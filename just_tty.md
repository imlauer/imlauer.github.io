---
title: "TTY, Linux Framebuffer, EGLFS and SDL - Without the weight of Xorg or Wayland"
date: 2025-09-13
---

Currently, I'm only using EGLFS with ttyd, I start my browser with the following script:


```bash
#!/bin/bash
sudo chmod 666 /dev/input/event*

ttyd --port 2020 --writable fish & 

falkon "http://localhost:2020"
```

And in `.config/fish/config.fish` I had:

```bash
if test -z "$TMUX" -a $XDG_VTNR = 1
  tmux attach || exec tmux new-session
end
export QT_QPA_PLATFORM=eglfs  
export XKB_DEFAULT_LAYOUT=es
set -U fish_greeting
```


#### **1. TTY Environment Setup**  
  
For efficient management of your terminals and processes, it is essential to use a terminal multiplexer.  
  
*   **Start a Terminal Multiplexer Upon Login:**  
    *   For `fish` shell, add to the `.config/fish/config.fish` file:  
  
```bash  
if test -z "$TMUX" -a $XDG_VTNR = 1
  tmux attach || exec tmux new-session
end
```  
This will automatically start `tmux` in the tty number 1 (a terminal multiplexer similar to `tmux`).        
**Alternatively, you can use `dvtm`.**
  
#### **2. Web Browsing from TTY**  
  
*   **Recommended Text Browsers:**  
    *   **w3m**: This browser supports displaying images directly in the console without an additional tool **you can render JavaScript only sites** using headless chromium save it as shell script and set it as external browser in w3m: `chromium --headless $1 --disable-gpu --run-all-compositor-stages-before-draw --dump-dom --virtual-time-budget=10000 | sed "s|<head>|<head><base href=$1>|g" | w3m -T text/html`. Scale of image %10.
    *   **[chawan](https://sr.ht/~bptato/chawan/)**.
    *   **Install `fbida`**:  
  
#### **3. Multimedia Viewing: Images, PDFs, and Videos**  
  
*   **View Images in TTY (with `fbi` and `mpv`):**  
    *   Install `fbida`: `pacman -S fbida`. You can use `fbi` (part of `fbida`) to view images: `fbi image.jpg` or `fim image.jpg`.
    *   `mpv` can also be used to view images.  
  
*   **Read PDFs from the TTY:**  
    *   **`fbpdf`**:  `fbpdf document_name.pdf`  
    *   Alternatively, you can use any KDE application to open a pdf too.  
  
*   **Watch Videos (YouTube, Twitch) from the TTY:**  
    *   **`w3m` with Invidious**:  
        *   Browse to Invidious (e.g., `inv.nadeko.net`) with `w3m`.  
        *   Configure `mpv` as the default browser in `w3m`. When accessing the video URL, press **`Shift+M`** to open it with `mpv` or **`Escape+Shift+M`**.
    *   **`mpv` for Twitch**:  
        *   You can use `mpv` to watch Twitch streams (you will have to run mpv with `--ignore-config` if you're using mpv with YouTube settings.  
    *   **Video Playback in DRM**:  `mpv --vo=drm video.mp4`  
    *   **`mpv` and `invidious` for YouTube**:  
        * `alias invidious 'w3m https://inv.nadeko.net/feed/subscriptions'` and set `mpv` as default browser.  

####  My `/etc/mpv/mpv.conf`:   
```bash  
$ cat /etc/mpv/mpv.conf  
--profile=fast  
--sub-auto=all  
--vo=drm
--ytdl-raw-options="format=bestvideo[height<=?360]+bestaudio/best[height<=?360]/bestvideo[height<=?480]+bestaudio/best[height<=?480],write-auto-sub=,sub-lang=[es,en,ru],write-sub="  
--volume-max=600  
#--save-position-on-quit  
#--untimed  
#--profile=low-latency  
--mute=yes  
```  

####  My `/etc/yt-dlp.conf`:  

```bash  
$ cat /etc/yt-dlp.conf  
--format=233+230  
--write-auto-sub  
--write-sub  
--sub-lang=en  
#--cookies-from-browser firefox  
```  

**Important**: If you use `mpv` for videos, run it outside `tmux`; otherwise, you won't be able to switch between other TTYs.  

*   **Search Torrents:**  
    *   Use `jackett` and `btstrm` to search for torrents from the console.  
  
#### **4. Using Lightweight Graphical Applications in TTY (FrameBuffer: `eglfs` and `linuxfb`)**  


*   **Set environment Variables for `eglfs` and `linuxfb`:**  
To enable/disable `gpu`.
```bash
#export QTWEBENGINE_CHROMIUM_FLAGS="--ignore-gpu-blacklist --disable-gpu"
export QTWEBENGINE_CHROMIUM_FLAGS="--ignore-gpu-blacklist"
```
* **Use `export XKB_DEFAULT_LAYOUT=es` to set your keyboard distribution.**  
*   To use `eglfs`:  
```bash  
export QT_QPA_PLATFORM=eglfs  
```  

Then, start your Qt application (e.g., `qutebrowser`).  

*  To use `linuxfb`:  
```bash  
export QT_QPA_PLATFORM=linuxfb:size=1000x1000  
```  

  
To run some applications that normally require a graphical server (like graphical web browsers), you can run it using `linuxfb` or `eglfs`.

#### Always open Qt apps inside a Terminal Multiplexer, otherwise when the application freezes your entire machine will freeze and you won't be able to use `Control+C`. 

##### In some Linux distributions, you need to run the following command to get the mouse and keyboard working:

```bash
sudo chmod 666 /dev/input/event*
```  


*   **Graphical Browsers** (with `eglfs`, `linuxfb` or `sdl` support):
    *   **`qutebrowser` (with `eglfs`):**  
        Or configure the `QT_QPA_PLATFORM` environment variable as indicated above.  
        *   **Copy/Paste in `qutebrowser`**: You can use `privatebin` to copy text from `qutebrowser`, then access the URL and save the file.  
    *   **`falkon`:**  
        *   It can be used with `eglfs`, although it did not work with `linuxfb` in one instance.  
        *   I use **Android as my User-Agent**: For pages to load faster:  
    *   **Ad Blocking in `Falkon` (it's no good)** so I use greasymonkey (still not good). 
	    1.  Go to `AdBlock settings`, and add all non-regional lists (EasyPrivacy, NoCoin List, Anti-Adblock Killer, Peter Lowe's List, etc.).  
	    2.  Go to `Settings -> Extensions`, and check the box for `GreaseMonkey`.  
	    3.  Install a YouTube ad-blocking script from `https://greasyfork.org`.
    *   **`Konqueror`**: It is a KDE browser that can also be tested in these configurations.  
    *   **`NetSurf`**: Can be run in tty using `SDL`: `netsurf-fb -f sdl -w 1366 -h 768`. `NetSurf` does not have JavaScript support. _You can add `netsurf-fb -f sdl -w 1366 -h 768` as external browser in `w3m`_.
*   **All KDE applications built with Qt can run from the TTY using these framebuffer platforms** like `kolourpaint` you can play games like `doom` also.
* Use `Control+Z` to get back to the TTY and `fg` to reopen the qt application.
  
* when using ffmpeg to record, you can capture any qt application with the `linuxfb` platform, but recording is not possible if you are using `elgfs`.  

```bash  
# You need to open the live dashboard first.  
  
falkon "https://www.youtube.com/live_dashboard"  
  
### Stream to YouTube only tty.  
ffmpeg -f alsa -i pipewire -thread_queue_size 1024 -f fbdev -framerate 60 -i /dev/fb0 -c:v libx264 -preset ultrafast -tune zerolatency -pix_fmt yuv420p -c:a aac -b:a 128k -f flv -async 1 -ar 48000 -latency 100 -bufsize 1000k rtmp://a.rtmp.youtube.com/live2/KEY 2> /dev/null  
  
#### Stream to YouTube TTY with camera.  
ffmpeg -f alsa -i pipewire -thread_queue_size 1024 -f fbdev -framerate 60 -i /dev/fb0 -f v4l2 -framerate 60 -video_size 320x240 -i /dev/video0 -filter_complex "[2:v]scale=320:240[cam];[1:v][cam]overlay=main_w-overlay_w-10:main_h-overlay_h-10[outv]" -map "[outv]" -map 0:a -c:v libx264 -preset ultrafast -tune zerolatency -pix_fmt yuv420p -c:a aac -b:a 128k -f flv -bufsize 1000k rtmp://a.rtmp.youtube.com/live2/KEY 2> /dev/null  
  
### Stream to YouTube full cam.  
ffmpeg -f alsa -i pipewire -thread_queue_size 1024 -f v4l2 -framerate 60 -video_size 1280x720 -i /dev/video0 -c:v libx264 -preset ultrafast -tune zerolatency -pix_fmt yuv420p -c:a aac -b:a 128k -f flv -bufsize 1000k rtmp://a.rtmp.youtube.com/live2/KEY 2> /dev/null  
  
### Record video.  
ffmpeg -f alsa -i pipewire -f fbdev -r 30 -i /dev/fb0 record.mp4  
  
```  
  
#### **5. Additional Tips and Useful Tools**  
  
*   **Mouse Usage in TTY:**  
    *   You need to use `GPM` to have mouse support in the TTY: `sudo systemctl start gpm`.  
  
*   **Copy and Paste Text from Graphical Browser:**  
    *   This is the solution I use I'm sure there's better: I use `ttyd` a web terminal, to copy text (e.g., from `qutebrowser`), paste it into `vim` in  ttyd.

My current alias for web-browsing:

```bash
alias dgg 'w3m  dgg.gg'
alias mojeek "w3m https://www.mojeek.com/search?q=hola"
alias wiby "w3m http://wiby.org"
alias news "netsurf-fb -f sdl -w 1366 -h 768 news.ycombinator.com"
alias doom 'cd doom; bash play_doom.sh;'
alias rcommandline "w3m old.reddit.com/r/commandline"
alias google 'w3m https://leta.mullvad.net/search?q=google&engine=google'
alias images="w3m https://pinterest.lurkmore.com/"
alias lyrics="w3m https://genius.lurkmore.com/"
```

#### Upload files from tty to archive.

```bash
python -m venv internetarchive
pip install internetarchive
source internetarchive/bin/activate.fish
ia upload tag *.jpg
ia metadata tag
```
