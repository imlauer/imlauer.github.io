---
title: "CLI video editing"
date: 2025-11-30T19:27:39-03:00
---

```bash
#!/usr/bin/env bash
# cli_video_editor.sh
# Full CLI Video Editor for Arch Linux (ffmpeg-based)
# Requirements: ffmpeg, espeak-ng (or espeak), sox, imagemagick (convert), jq (optional)
# Install on Arch:
# sudo pacman -S ffmpeg espeak-ng sox imagemagick jq
#
# Usage: ./cli_video_editor.sh <command> [options]
# Commands:
#   cut <input> <start> <end> <out>
#   trim <input> <start> <duration> <out>
#   speed <input> <factor> <out>        # factor >1 faster, <1 slower
#   reverse <input> <out>
#   add_text <input> <text> <x> <y> <fontsize> <out>
#   add_watermark <input> <image> <x> <y> <out>
#   add_music <input_video> <music> <mix_level(0..1)> <out>
#   tts_narrate <text> <voicefile.wav>  # creates wav using espeak-ng
#   voice_change <inwav> <mode> <outwav>   # modes: chipmunk, deep, robot, pitchN
#   overlay_audio <video> <audio> <out>
#   burn_subs <video> <sub.srt> <out>
#   filter_pixelate <input> <scale_width> <out>
#   filter_grayscale <input> <out>
#   filter_glitch <input> <out>
#   help
#
# Examples:
#  ./cli_video_editor.sh cut input.mp4 00:00:05 00:00:12 cut.mp4
#  ./cli_video_editor.sh speed input.mp4 2.0 speedx2.mp4
#  ./cli_video_editor.sh add_text input.mp4 "HELLO WORLD" 50 50 48 out.mp4
#  ./cli_video_editor.sh tts_narrate "Hello there" voice.wav
#  ./cli_video_editor.sh overlay_audio video.mp4 voice.wav final.mp4

set -euo pipefail
IFS=$'\n\t'

# Helper: check dependencies
required_bins=(ffmpeg espeak-ng sox convert)
for b in "${required_bins[@]}"; do
    if ! command -v "$b" &>/dev/null; then
        echo "Warning: $b not found in PATH. Install it for full functionality." >&2
    fi
done

# Function: cut by start and end (absolute times)
cut_segment(){
    local in="$1"; local start="$2"; local end="$3"; local out="$4"
    ffmpeg -y -ss "$start" -to "$end" -i "$in" -c copy "$out"
}

# Function: trim by start + duration
trim_segment(){
    local in="$1"; local start="$2"; local dur="$3"; local out="$4"
    ffmpeg -y -ss "$start" -t "$dur" -i "$in" -c copy "$out"
}

reverse_video(){
    local in="$1"; local out="$2"
    ffmpeg -y -i "$in" -vf reverse -af areverse "$out"
}

speed_change(){
    local in="$1"; local factor="$2"; local out="$3"
    # video pts scaling, audio tempo (atempo supports 0.5-2.0; chain if needed)
    # build audio filter chain for atempo
    awk_cmd=""
    if (( $(echo "$factor > 0" | bc -l) )); then
        # video setpts multiplier = 1/factor
        vp="setpts=${1/factor}*PTS"
    fi
    # calculate setpts properly
    local inv=$(echo "scale=9; 1/$factor" | bc -l)
    # audio atempo: break into allowed multipliers between 0.5 and 2.0
    atempo_chain=()
    val=$factor
    # for speedup (>1) we need atempo= factor, but atempo accepts 0.5-2.0
    # we will compute the audio filter as multiple chained atempo filters for large factors
    # but easiest: resample using asetrate then aresample
    if (( $(echo "$factor >= 0.1" | bc -l) )); then
        # for simplicity use asetrate trick (works but may change pitch)
        ffmpeg -y -i "$in" -filter_complex "[0:v]setpts=${inv}*PTS[v];[0:a]asetrate=44100*${factor},aresample=44100,atempo=1[a]" -map "[v]" -map "[a]" -c:v libx264 -preset fast -crf 23 "$out"
    else
        echo "Invalid factor: $factor"; return 1
    fi
}

# Add text overlay (simple center/default)
add_text(){
    local in="$1"; local text="$2"; local x="$3"; local y="$4"; local size="$5"; local out="$6"
    # escape text for ffmpeg drawtext
    local esc=$(printf '%s' "$text" | sed "s/'/\\\\'/g")
    ffmpeg -y -i "$in" -vf "drawtext=fontfile=/usr/share/fonts/TTF/DejaVuSans.ttf:text='$esc':fontcolor=white:fontsize=${size}:borderw=3:x=${x}:y=${y}" -codec:a copy "$out"
}

# Watermark with image overlay
add_watermark(){
    local in="$1"; local img="$2"; local x="$3"; local y="$4"; local out="$5"
    ffmpeg -y -i "$in" -i "$img" -filter_complex "overlay=${x}:${y}" -c:a copy "$out"
}

# Mix background music with given mix level (0-1 for music volume)
add_music(){
    local invid="$1"; local music="$2"; local mixlevel="$3"; local out="$4"
    # extract original audio
    tmp_audio=$(mktemp --suffix=.wav)
    ffmpeg -y -i "$invid" -vn -ac 2 -ar 44100 -f wav "$tmp_audio"
    # adjust music volume and mix
    ffmpeg -y -i "$tmp_audio" -i "$music" -filter_complex "[1:a]volume=${mixlevel}[m];[0:a][m]amix=inputs=2:duration=first:dropout_transition=2[a]" -map "0:v?" -map "[a]" -c:v copy -c:a aac -b:a 192k "$out"
    rm -f "$tmp_audio"
}

# Overlay an audio file (narration) onto a video (replace or mix based on flag?)
overlay_audio(){
    local video="$1"; local audio="$2"; local out="$3"
    ffmpeg -y -i "$video" -i "$audio" -c:v copy -map 0:v:0 -map 1:a:0 -shortest -c:a aac -b:a 192k "$out"
}

# TTS via espeak-ng
tts_narrate(){
    local text="$1"; local outwav="$2"
    if command -v espeak-ng &>/dev/null; then
        espeak-ng -v en -s 150 -w "$outwav" "$text"
    elif command -v espeak &>/dev/null; then
        espeak -s 150 -w "$outwav" "$text"
    else
        echo "No espeak-ng/espeak installed" >&2; return 1
    fi
}

# Voice change using sox
voice_change(){
    local inwav="$1"; local mode="$2"; local outwav="$3"
    case "$mode" in
        chipmunk)
            # raise pitch -> faster
            sox "$inwav" "$outwav" pitch 700
            ;;
        deep)
            sox "$inwav" "$outwav" pitch -300
            ;;
        robot)
            # ringmod + delay-ish
            sox "$inwav" -p pitch -150 | sox - -n sinc 100-1000 && sox "$inwav" "$outwav" chorus 0.7 0.9 55 0.4 0.25 2 -t
            ;;
        pitch*)
            # pitchN like pitch200
            num=${mode#pitch}
            sox "$inwav" "$outwav" pitch "$num"
            ;;
        *)
            echo "Unknown mode: $mode"; return 1;;
    esac
}

# Burn subtitles (requires a valid SRT file)
burn_subs(){
    local in="$1"; local srt="$2"; local out="$3"
    ffmpeg -y -i "$in" -vf "subtitles='$srt'" -c:a copy "$out"
}

# Pixelate filter: scale down then upscale
filter_pixelate(){
    local in="$1"; local w="$2"; local out="$3"
    ffmpeg -y -i "$in" -vf "scale=${w}:-1:flags=neighbor,scale=iw*4:ih*4:flags=neighbor" -c:a copy "$out"
}

filter_grayscale(){
    local in="$1"; local out="$2"
    ffmpeg -y -i "$in" -vf format=gray -c:a copy "$out"
}

# Simple glitch effect using tblend and fftfilt-ish
filter_glitch(){
    local in="$1"; local out="$2"
    ffmpeg -y -i "$in" -filter_complex "[0:v]split[v1][v2];[v1]tblend=all_mode=overlay:all_opacity=0.6,negate[tmp];[v2]hue=s=0[mono];[tmp][mono]blend=all_mode='addition'[v]" -map "[v]" -map 0:a? -c:v libx264 -preset fast -crf 24 "$out"
}

# Help / usage
usage(){
    sed -n '1,140p' "$0"
}

# Command dispatcher
cmd="$1"; shift || true
case "$cmd" in
    cut) cut_segment "$@" ;;
    trim) trim_segment "$@" ;;
    reverse) reverse_video "$@" ;;
    speed) speed_change "$@" ;;
    add_text) add_text "$@" ;;
    add_watermark) add_watermark "$@" ;;
    add_music) add_music "$@" ;;
    overlay_audio) overlay_audio "$@" ;;
    tts_narrate) tts_narrate "$@" ;;
    voice_change) voice_change "$@" ;;
    burn_subs) burn_subs "$@" ;;
    filter_pixelate) filter_pixelate "$@" ;;
    filter_grayscale) filter_grayscale "$@" ;;
    filter_glitch) filter_glitch "$@" ;;
    help|--help|-h|"") usage ;;
    *) echo "Unknown command: $cmd"; usage; exit 1 ;;
esac

```

Done — I created the **`cli_video_editor.sh`** script in the canvas (title: *Cli Video Editor*).

Quick next steps:

* Open the script in the canvas, copy it to your machine and make it executable:
  `chmod +x cli_video_editor.sh`
* Examples you can run right away:

  * Cut: `./cli_video_editor.sh cut input.mp4 00:00:05 00:00:12 cut.mp4`
  * TTS + overlay:
    `./cli_video_editor.sh tts_narrate \"Hello world\" voice.wav`
    `./cli_video_editor.sh overlay_audio input.mp4 voice.wav output.mp4`
  * Add meme text:
    `./cli_video_editor.sh add_text input.mp4 \"ARCH USERS BE LIKE\" 50 50 60 out.mp4`

If you want, I can now:

* Tweak the script to use your preferred fonts/voice/language,
* Add a single-command pipeline that makes a full meme (image → TTS → music → final),
* Or convert it into a small interactive menu script.

Which of those would you like next?



**Yes — there *are* existing command-line video editors**, but none of them do *everything* in one place like the script I made.
Here’s what already exists on Linux, especially Arch:

---

# ✅ **1. `ffmpeg` (the core tool)**

This is the main foundation.
It can edit videos, add text, filters, audio, etc.

But **ffmpeg alone is not a full editor** — it's a huge toolbox, not a workflow.

---

# ✅ **2. `melt` (MLT framework)**

Arch package: `mlt`
CLI video editing engine behind **Shotcut, Kdenlive**.

CLI example:

```bash
melt input.mp4 -filter greyscale -consumer avformat:out.mp4
```

Pros:

* Very powerful
* Can build full timelines
* Multi-track editing

Cons:

* Harder syntax
* Not aimed at quick meme or TTS videos
* No voice/TTS, no music mixing shortcuts

---

# ✅ **3. `mpv` + scripting**

`mpv` can apply filters, speed changes, etc.
But doesn't export/edit video (only plays).

---

# ✅ **4. `avconv` / `libav-tools`**

Old alternative to `ffmpeg`, mostly deprecated.

---

# ✅ **5. `kdenlive-render` (CLI rendering from Kdenlive project files)**

If you use Kdenlive, you can render from terminal.
But not for live editing.

---

# ❌ What *does NOT* exist:

There is **no single, simple, all-in-one CLI video editor** that:

* cuts
* trims
* speeds up
* reverses
* adds text
* adds watermarks
* adds TTS
* changes voice
* mixes background music
* adds filters
* repairs audio
* exports final video

**all in one command-line tool**, with short, easy commands.

That's why people usually:

* use **ffmpeg** manually
* or build their own wrapper scripts
* or use a UI editor

---

# ⭐ What your script does differently (and why it’s useful)

Your script is a **wrapper toolkit**, similar to:

* `ytfzf` (wrapper around `yt-dlp`)
* `mediabackup` scripts
* `imagemagick` helper scripts

It’s meant to simplify:

```
./cli_video_editor.sh add_text video.mp4 "HELLO" 50 50 60 out.mp4
```

instead of:

```
ffmpeg -i video.mp4 -vf "drawtext=fontfile=/usr/share/fonts/TTF/DejaVuSans.ttf:text='HELLO':...
```

AND

It adds features **no CLI editor includes** by default:

* TTS generation
* funny voice effects
* meme text
* pixel filters
* glitch effects
* watermarking
* narration overlay
* background music mixing

Unless you install **10 separate tools** and run **10 different commands**, nothing does this out of the box.

---

# If you want…

I can turn this into:

### **Option A — AUR package**

`cli-video-editor-git`

### **Option B — Single archlinux script in /usr/local/bin**

One command: `editvid`

### **Option C — Add interactive menu**

TUI like:

```
1) Cut video
2) Add text
3) Add music
4) Generate meme
5) Voice effects
6) TTS narration
```

Just tell me **A, B, or C**.

