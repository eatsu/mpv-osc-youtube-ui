# mpv-osc-youtube-ui

This is an [mpv](https://github.com/mpv-player/mpv) OSC script with YouTube-like UI/UX, based on [mpv-osc-modern](https://github.com/maoiscat/mpv-osc-modern).

![preview](preview.png?raw=true)

## Changes from mpv-osc-modern

- YouTube-like UI
- More compact layout
- Hover effect for buttons
- Softer black gradient background
- Fade-in effect on popup
- Shorter duration for fade-in/out
- No deadzone (OSC will show up anywhere in the window with mouse movement)
- No window controls when full screen

## Installation

1. Install `youtube-ui.lua` into `~/.config/mpv/scripts`:

```sh
mkdir -p ~/.config/mpv/scripts
wget -P ~/.config/mpv/scripts https://github.com/eatsu/mpv-osc-youtube-ui/raw/main/youtube-ui.lua
```

2. Install `Material-Design-Iconic-Font.ttf` into `~/.local/share/fonts`:

```sh
mkdir -p ~/.local/share/fonts
wget -P ~/.local/share/fonts https://github.com/eatsu/mpv-osc-youtube-ui/raw/main/Material-Design-Iconic-Font.ttf
```

3. Add the following lines to the end of `~/.config/mpv/mpv.conf`:

```conf
osc=no

[Idle]
profile-cond=p["idle-active"]
profile-restore=copy-equal
title=' '
keepaspect=no
background=1
```

4. (optional) Install `thumbfast.lua` from [thumbfast](https://github.com/po5/thumbfast) into `~/.config/mpv/scripts`:

```sh
wget -P ~/.config/mpv/scripts https://github.com/po5/thumbfast/raw/master/thumbfast.lua
```
