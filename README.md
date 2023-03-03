# mpv-osc-youtube-ui

This is an [mpv](https://mpv.io) OSC script based on
[mpv-osc-modern](https://github.com/maoiscat/mpv-osc-modern) that provides a YouTube-like UI.

![preview](preview.png?raw=true)

## Changes from mpv-osc-modern

- YouTube-like UI
- More compact layout
- Larger clickable area of buttons
- Hover effect for buttons
- Softer black gradient background
- Fade-in effect on popup
- Shorter duration for fade-in/out
- No deadzone by default (OSC will show up anywhere in the window with mouse movement)
- No window controls when full screen
- Using built-in icons instead of the iconic font

## Installation

1. Put `youtube-ui.lua` in your mpv `scripts` directory:

```sh
mkdir -p ~/.config/mpv/scripts
wget -P ~/.config/mpv/scripts https://github.com/eatsu/mpv-osc-youtube-ui/raw/main/youtube-ui.lua
```

2. Add `osc=no` to your `mpv.conf` file:

```sh
echo 'osc=no' >> ~/.config/mpv/mpv.conf
```

3. (optional) Put `thumbfast.lua` from [thumbfast](https://github.com/po5/thumbfast) in your mpv
`scripts` directory:

```sh
wget -P ~/.config/mpv/scripts https://github.com/po5/thumbfast/raw/master/thumbfast.lua
```

## Credits

- The main script is based on [mpv-osc-modern](https://github.com/maoiscat/mpv-osc-modern) and
  mpv's [`osc.lua`](https://github.com/mpv-player/mpv/blob/master/player/lua/osc.lua).
- `svgtohtmltoluapath.py` is based on [mpv-osc-tethys](https://github.com/Zren/mpv-osc-tethys).
- Icons are based on [material-design-icons](https://github.com/google/material-design-icons).
