---
title: "Instagram Shorts with FFMpeg"
date: 2025-12-20T02:03:13-03:00
---

# Claude

I'll help you create a tool to detect potential viral moments from Twitch VODs and create Instagram reels with burned-in subtitles using FFmpeg!

Here's a comprehensive approach:

## Strategy for Detecting Viral Moments

Since FFmpeg alone can't "detect" viral content (it needs AI/ML for that), I'll show you how to:

1. **Use FFmpeg's scene detection** to find interesting transitions/moments
2. **Detect audio peaks** (loud reactions, excitement)
3. **Extract segments** and add burned-in subtitles
4. **Format for Instagram Reels** (9:16 aspect ratio, 15-90 seconds)

## Step-by-Step FFmpeg Commands

### 1. Detect Scene Changes & Audio Peaks

```bash
# Detect scenes with significant changes
ffmpeg -i input.mp4 -filter_complex \
"[0:v]select='gt(scene,0.4)',metadata=print:file=scenes.txt[out]" \
-map "[out]" -f null -

# Detect audio peaks (loud moments)
ffmpeg -i input.mp4 -af "volumedetect" -f null - 2>&1 | grep "max_volume"
```

### 2. Extract Specific Segment (e.g., 30 seconds starting at 5:23)

```bash
ffmpeg -ss 00:05:23 -i input.mp4 -t 30 -c copy segment.mp4
```

### 3. Generate Subtitles (You'll need a subtitle file first)

For auto-subtitles, you'd need to use Whisper or similar tool first:
```bash
# If you have whisper installed
whisper segment.mp4 --model base --output_format srt
```

### 4. Crop to 9:16 (Instagram Reel format) + Burn Subtitles

```bash
ffmpeg -i segment.mp4 -vf "crop=ih*9/16:ih,scale=1080:1920,subtitles=segment.srt:force_style='Alignment=10,FontSize=24,MarginV=100,Bold=1,OutlineColour=&H000000&,Outline=2'" \
-c:v libx264 -preset medium -crf 23 -c:a aac -b:a 128k reel_output.mp4
```

### 5. All-in-One Command (with timestamp)

```bash
ffmpeg -ss 00:05:23 -i input.mp4 -t 30 \
-vf "crop=ih*9/16:ih,scale=1080:1920,subtitles=segment.srt:force_style='Alignment=10,FontSize=28,MarginV=120,Bold=1,PrimaryColour=&HFFFFFF&,OutlineColour=&H000000&,Outline=3,Shadow=2'" \
-c:v libx264 -preset medium -crf 23 -pix_fmt yuv420p \
-c:a aac -b:a 128k -ar 48000 \
-movflags +faststart \
reel_final.mp4
```

## Advanced: Automated Viral Moment Detection Script

Let me create a bash script that combines these techniques:## Key Features Explained

**Subtitle Styling Options:**
- `Alignment=10` - Bottom center (2=bottom, 10=top center)
- `FontSize=32` - Adjust based on preference
- `Bold=1` - Bold text for readability
- `OutlineColour=&H000000&` - Black outline (hex in BGR format)
- `Outline=4` - Thick outline for contrast
- `MarginV=150` - Distance from bottom (pixels)

**Finding Viral Moments (Manual Analysis):**
1. **Watch for chat reactions** in VOD
2. **Look at view count spikes** on Twitch stats
3. **Use audio analysis** - sudden volume increases often indicate exciting moments
4. **Scene detection** - rapid scene changes can indicate action

**Better Automation Options:**
- Use **Whisper AI** for auto-transcription
- Use **FFmpeg's `silencedetect`** to find reaction gaps
- Parse **Twitch chat replay** for emote spikes (requires external tool)
- Use **ML models** like PySceneDetect for better scene analysis

**Instagram Reel Requirements:**
- ✅ 9:16 aspect ratio (1080x1920)
- ✅ 15-90 seconds duration
- ✅ H.264 codec
- ✅ AAC audio
- ✅ faststart flag for quick loading

Would you like me to create a more advanced version with Python that includes actual ML-based viral moment detection, or help you set up Whisper for automatic subtitle generation?



```bash
#!/bin/bash

# Twitch VOD to Instagram Reel with Viral Moment Detection
# Usage: ./vod_to_reel.sh input.mp4 [start_time] [duration]

INPUT="$1"
START_TIME="${2:-00:00:00}"
DURATION="${3:-30}"

if [ -z "$INPUT" ]; then
    echo "Usage: $0 input.mp4 [start_time] [duration]"
    echo "Example: $0 stream.mp4 00:15:30 45"
    exit 1
fi

# Output filename
OUTPUT="reel_$(date +%Y%m%d_%H%M%S).mp4"
TEMP_SEGMENT="temp_segment.mp4"
SRT_FILE="temp_segment.srt"

echo "🎬 Processing Twitch VOD to Instagram Reel..."

# Step 1: Detect loud moments (potential viral content)
echo "📊 Analyzing audio for peak moments..."
ffmpeg -i "$INPUT" -af "volumedetect,silencedetect=noise=-30dB:d=0.5" -f null - 2>&1 | tee audio_analysis.log

# Step 2: Extract segment
echo "✂️  Extracting segment from $START_TIME (${DURATION}s)..."
ffmpeg -ss "$START_TIME" -i "$INPUT" -t "$DURATION" -c copy "$TEMP_SEGMENT" -y

# Step 3: Generate subtitles (requires whisper)
echo "📝 Generating subtitles..."
if command -v whisper &> /dev/null; then
    whisper "$TEMP_SEGMENT" --model base --output_format srt --output_dir . 2>/dev/null
    mv temp_segment.srt "$SRT_FILE" 2>/dev/null || echo "⚠️  No subtitle file generated"
else
    echo "⚠️  Whisper not installed. Skipping subtitle generation."
    echo "   Install: pip install openai-whisper"
fi

# Step 4: Convert to 9:16 format with subtitles
echo "🎨 Converting to Instagram Reel format (9:16)..."

if [ -f "$SRT_FILE" ]; then
    # With subtitles
    ffmpeg -i "$TEMP_SEGMENT" \
        -vf "crop=ih*9/16:ih,scale=1080:1920,subtitles='$SRT_FILE':force_style='Alignment=10,FontName=Arial,FontSize=32,Bold=1,PrimaryColour=&HFFFFFF&,OutlineColour=&H000000&,Outline=4,Shadow=2,MarginV=150'" \
        -c:v libx264 -preset medium -crf 23 -pix_fmt yuv420p \
        -c:a aac -b:a 128k -ar 48000 \
        -movflags +faststart \
        "$OUTPUT" -y
else
    # Without subtitles
    ffmpeg -i "$TEMP_SEGMENT" \
        -vf "crop=ih*9/16:ih,scale=1080:1920" \
        -c:v libx264 -preset medium -crf 23 -pix_fmt yuv420p \
        -c:a aac -b:a 128k -ar 48000 \
        -movflags +faststart \
        "$OUTPUT" -y
fi

# Cleanup
rm -f "$TEMP_SEGMENT" "$SRT_FILE"

echo "✅ Done! Output: $OUTPUT"
echo ""
echo "📱 Instagram Reel specs:"
ffprobe -v quiet -print_format json -show_format -show_streams "$OUTPUT" | grep -E "(width|height|duration|codec_name)" | head -6

# Optional: Show scene detection results
echo ""
echo "💡 To find viral moments automatically, analyze the audio_analysis.log file"
echo "   Look for: high volume peaks, silence breaks (reactions), or use the timestamps"
```


---


```bash
The error you're seeing is because **WebM format only supports VP8, VP9, or AV1 video codecs** (and Vorbis/Opus for audio), but you're trying to encode with **libx264 (H.264)** which is not compatible with WebM containers.

## Solution: Change the output format or codec

**Option 1: Change to MP4 (recommended for H.264)**
```bash
ffmpeg -ss 00:05:23 -i "winning.webm" -t 30 \
  -vf "crop=ih*9/16:ih,scale=1080:1920,subtitles=sub.srt:force_style='Alignment=10,FontSize=28,MarginV=120,Bold=1,PrimaryColour=&HFFFFFF&,OutlineColour=&H000000&,Outline=3,Shadow=2'" \
  -c:v libx264 -preset medium -crf 23 -pix_fmt yuv420p \
  -c:a aac -b:a 128k -ar 48000 \
  -movflags +faststart reel_final.mp4
```

**Option 2: Keep WebM format with VP9 codec**
```bash
ffmpeg -ss 00:05:23 -i "winning.webm" -t 30 \
  -vf "crop=ih*9/16:ih,scale=1080:1920,subtitles=sub.srt:force_style='Alignment=10,FontSize=28,MarginV=120,Bold=1,PrimaryColour=&HFFFFFF&,OutlineColour=&H000000&,Outline=3,Shadow=2'" \
  -c:v libvpx-vp9 -b:v 2M -crf 30 -pix_fmt yuv420p \
  -c:a libopus -b:a 128k -ar 48000 \
  reel_final.webm
```

**Key changes for WebM:**
- Video codec: `libvpx-vp9` instead of `libx264`
- Audio codec: `libopus` instead of `aac`
- Use `-b:v 2M` and `-crf 30` for VP9 quality control

For social media reels (Instagram/TikTok), **MP4 with H.264 is usually the better choice** as it has wider compatibility.
```

---

```bash
ffmpeg -ss 00:05:23 -i "fiUMZTFIp3s.mp4" -t 30 -vf "crop=ih*9/16:ih,scale=1080:1920,subtitles=sub.srt:force_style='Alignment=10,FontSize=28,MarginV=120,Bold=1,PrimaryColour=&HFFFFFF&,OutlineColour=&H000000&,Outline=3,Shadow=2'" -c:v libx264 -preset medium -crf 23 -pix_fmt yuv420p -c:a aac -b:a 128k -ar
48000 -movflags +faststart reel_final.mp4
```


