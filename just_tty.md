---
title: "Unleashing the Power: TTY, Linux Framebuffer, and EGLFS - Without the weight of Xorg or Wayland"
date: 2025-09-13
---

### **Tutorial: Live Exclusively from the TTY (Without Xorg or Wayland)**

This tutorial will guide you to perform common and advanced tasks directly from the Terminal (TTY), leveraging console tools and the framebuffer.

#### **1. TTY Environment Setup**

For efficient management of your terminals and processes, it is essential to use a terminal multiplexer.

*   **Start a Terminal Multiplexer Upon Login:**
    *   For `fish` shell, add to the `.config/fish/config.fish` file:
        ```bash
        if status --is-login
            if test -z "$DISPLAY" -a $XDG_VTNR = 1
                exec tmux
            end
        end
        ```
        This will automatically start `tmux` (a terminal multiplexer similar to `tmux`) if no graphical environment is running.
    *   Alternatively, you can use `dvtm`.

#### **2. Web Browsing from TTY**

To browse the internet, you will use text-based browsers. For multimedia content, you will need additional tools.

*   **Recommended Text Browsers:**
    *   **w3m**: `w3m`. This browser supports displaying images directly in the console without an additional tool **you can render JavaScript only sites** using this: `chromium --headless $1 --disable-gpu --run-all-compositor-stages-before-draw --dump-dom --virtual-time-budget=10000 | sed "s|<head>|<head><base href=$1>|g" | w3m -T text/html`.
    *   **elinks**: use fbi to view images.
    *   **lynx**: `lynx`.
    *   **links 2**: `links 2`. Apparently, `links 2` has better JavaScript support; the recommendation is to install all of them.

*   **Configuration for `lynx` (accept cookies):**
    *   Edit the configuration file:
        ```bash
        sudo vim /etc/lynx.cfg
        ```
    *   Uncomment line 1359 and set its value to `TRUE`:
        ```
        ACCEPT_ALL_COOKIES:TRUE
        ```
        This allows `lynx` to accept all cookies by default.

*   **Image Support in `elinks` and `lynx`:**
    *   **Install `fbida`**:
        ```bash
        # For Arch Linux (example, may vary depending on your distro)
        sudo pacman -S fbida
        ```
        `fbida` comes with a set of commands: `fbi`, `ida`. You need to configure `elinks` to open images using these programs.
    *   **Configure `elinks`**: Configure `elinks` to open images using `fbi` or `ida`.
    *   **Improve `elinks` display**: Set `elinks` to 16-bit colors in `Setup - Terminal Options - Color mode`.

*   **Basic JavaScript Support in `elinks`:**
    *   `elinks` has basic JavaScript support, enough for sites like 4chan. To add JavaScript support, you can follow guides like the one mentioned in the sources.

#### **3. Multimedia Viewing: Images, PDFs, and Videos**

*   **View Images in TTY (with `fbi` and `mpv`):**
    *   You can use `fbi` (part of `fbida`) to view images.
    *   `mpv` can also be used to view images.

*   **Read PDFs from the TTY:**
    *   **`fbpdf`**:
        ```bash
        fbpdf document_name.pdf
        ```
        `fbpdf` is the recommended tool for reading PDFs directly in the framebuffer.
    *   Alternatively, you can download the PDF with `w3m` and then use a viewer like `fbpdf`.

*   **Watch Videos (YouTube, Twitch, Kick) from the TTY:**
    *   **`w3m` with Invidious**:
        *   Browse to Invidious (e.g., `inv.nadeko.net`) with `w3m`.
        *   Configure `mpv` as the default browser in `w3m`. When accessing the video URL, press **`Shift+M`** to open it with `mpv`.
    *   **`mpv` for Twitch or Kick**:
        *   You can use `mpv` to watch Twitch or Kick streams.
    *   **Video Playback in Framebuffer**:
        *   When using `mpv` to watch videos from the framebuffer:
            ```bash
            mpv --vo=drm video.mp4
            ```
            This uses the framebuffer driver for video output.

    *   **`mpv` and `invidious` for YouTube**:
        * `alias invidious 'w3m https://inv.nadeko.net/feed/subscriptions'` and set `mpv` as default browser.
	*  This is my `mpv.conf`: 
```bash
$ cat /etc/mpv/mpv.conf
--profile=fast
--sub-auto=all
--ytdl-raw-options="format=bestvideo[height<=?360]+bestaudio/best[height<=?360]/bestvideo[height<=?480]+bestaudio/best[height<=?480],write-auto-sub=,sub-lang=[es,en,ru],write-sub="
--volume-max=600
#--save-position-on-quit
#--untimed
#--profile=low-latency
--mute=yes
```
	* `yt-dlp.conf`:
```bash
cat /etc/yt-dlp.conf
--format=233+230
--write-auto-sub
--write-sub
--sub-lang=en
#--cookies-from-browser firefox
```
	**Important**: If you use `mpv` for videos, run it without `tmux`; otherwise, you won't be able to switch between other TTYs.
*   **Search Torrents:**
    *   Use `jackett` and `btstrm` to search for torrents from the console.

#### **4. Using Lightweight Graphical Applications in TTY (FrameBuffer: `eglfs` and `linuxfb`)**

To run some applications that normally require a graphical server (like graphical web browsers), you can force them to use the framebuffer. This is especially useful on slow computers.
In some Linux distributions, you need to run the following command to get the mouse and keyboard working: `sudo chmod 666 /dev/input/event*`

*   **Concept of `eglfs` and `linuxfb`:**
    *   These platforms (Qt QPA drivers) allow Qt applications to take direct control of the mouse and keyboard and draw directly to the framebuffer, without an Xorg or Wayland server.
    *   **All KDE applications built with Qt can run from the TTY using these framebuffer platforms**. Since KDE applications are built with the Qt toolkit, they can leverage `eglfs` or `linuxfb` to render directly on the console.
    *   **Warning with `eglfs`**: **It is a bad idea because if the application crashes, you cannot close it and have to shut down the computer. DO NOT use it.**. This implies that trying to stop it with `Control+Z` is also not recommended and could lead to system freezes.

*   **Environment Variables for `eglfs` and `linuxfb`:**
    * Use `export XKB_DEFAULT_LAYOUT=es` to set your keyboard distribution.
    *   To use `eglfs`:
        ```bash
        export QT_QPA_PLATFORM=eglfs
        ```
        Then, start your Qt application (e.g., `qutebrowser`).
    *   To use `linuxfb`:
        ```bash
        export QT_QPA_PLATFORM=linuxfb:size=1000x1000
        ```
	* when using ffmpeg to record, you can capture any qt application with the `linuxfb` option, but recording is not possible if you are using `elgfs`.
```bash
# You need to open with site first.

falkon "https://www.youtube.com/live_dashboard"

### Stream only tty
ffmpeg -f alsa -i pipewire -thread_queue_size 1024 -f fbdev -framerate 60 -i /dev/fb0 -c:v libx264 -preset ultrafast -tune zerolatency -pix_fmt yuv420p -c:a aac -b:a 128k -f flv -async 1 -ar 48000 -latency 100 -bufsize 1000k rtmp://a.rtmp.youtube.com/live2/KEY 2> /dev/null

#### Stream TTY with camera.
#ffmpeg -f alsa -i pipewire -thread_queue_size 1024 -f fbdev -framerate 60 -i /dev/fb0 -f v4l2 -framerate 60 -video_size 320x240 -i /dev/video0 -filter_complex "[2:v]scale=320:240[cam];[1:v][cam]overlay=main_w-overlay_w-10:main_h-overlay_h-10[outv]" -map "[outv]" -map 0:a -c:v libx264 -preset ultrafast -tune zerolatency -pix_fmt yuv420p -c:a aac -b:a 128k -f flv -bufsize 1000k rtmp://a.rtmp.youtube.com/live2/KEY 2> /dev/null

### Full cam.
#ffmpeg -f alsa -i pipewire -thread_queue_size 1024 -f v4l2 -framerate 60 -video_size 1280x720 -i /dev/video0 -c:v libx264 -preset ultrafast -tune zerolatency -pix_fmt yuv420p -c:a aac -b:a 128k -f flv -bufsize 1000k rtmp://a.rtmp.youtube.com/live2/KEY 2> /dev/null

```
        In some cases, you may need to add specific flags for `falkon` and `qutebrowser` to work with `linuxfb`.

*   **Graphical Browsers that Support Framebuffer (examples of Qt apps):**
    *   **`qutebrowser` (with `eglfs`):**
        ```bash
        qutebrowser
        ```
        Or configure the `QT_QPA_PLATFORM` environment variable as indicated above.
        *   **Copy/Paste in `qutebrowser`**: You can use `privatebin` to copy text from `qutebrowser`, then access the URL and save the file.
    *   **`falkon`:**
        *   It can be used with `eglfs`, although it did not work with `linuxfb` in one instance.
        *   I use **Android as my User-Agent**: For pages to load faster:
            ```bash
            # This is configured in Falkon Preferences, in the last option.
            # You can use the Android User-Agent so Twitch loads faster.
            ```.
        *   **Ad Blocking in `Falkon`**:
            1.  Go to `AdBlock settings`, and add all non-regional lists (EasyPrivacy, NoCoin List, Anti-Adblock Killer, Peter Lowe's List, etc.).
            2.  Go to `Settings -> Extensions`, and check the box for `GreaseMonkey`.
            3.  Install a YouTube ad-blocking script from `https://greasyfork.org/en/scripts/459541-youtube   -youtube-ad-blocker`.
    *   **`Konqueror`**: It is a KDE browser that can also be tested in these configurations.
    *   **`NetSurf`**: Can be run in framebuffer mode: `netsurf-fb -f sdl -w 1366 -h 768`. `NetSurf` does not have JavaScript support. You can add `netsurf-fb -f sdl -w 1366 -h 768` as external browser in `w3m`.

#### **5. Additional Tips and Useful Tools**

*   **Mouse Usage in TTY:**
    *   You need to use `GPM` to have mouse support in the TTY: `sudo systemctl start gpm`.

*   **Copy and Paste Text:**
    *   This is the solution I use I'm sure there's better: I use `privatebin`, you can copy text (e.g., from `qutebrowser`), paste it into `privatebin`, get the URL, and then access it to save the file.
    *   For copy and paste in `vim` (if used in a Wayland environment as a reference, though not a direct TTY case): Select the lines to copy, press `Control+@`, and paste with `Control+Shift+V`.
