# mpv-osc-youtube-ui

An OSC script for [mpv](https://mpv.io) that provides a YouTube-like UI,
forked from [mpv-osc-modern](https://github.com/maoiscat/mpv-osc-modern).

![preview](preview.png?raw=true)
![preview-complex](preview-complex.png?raw=true)

## Notable changes from mpv-osc-modern

- YouTube-like UI
- More compact layout
- Larger clickable area of buttons
- Hover effect for buttons
- Softer black gradient background
- Fade-in effect on popup
- Shorter duration for fade-in/out
- No deadzone by default (OSC will show up anywhere in the window with mouse movement)
- No window controls when full screen
- Using built-in icons instead of the extra iconic font

## Installation

1. To disable the default OSC, add `osc=no` to your `mpv.conf` file:

```sh
echo 'osc=no' >> ~/.config/mpv/mpv.conf
```

2. Put `youtube-ui.lua` in your mpv `scripts` directory:

```sh
wget -P ~/.config/mpv/scripts https://github.com/eatsu/mpv-osc-youtube-ui/raw/main/youtube-ui.lua
```

3. (optional, but recommended) To show the thumbnail tooltip, put `thumbfast.lua` from
[thumbfast](https://github.com/po5/thumbfast) in your mpv `scripts` directory:

```sh
wget -P ~/.config/mpv/scripts https://github.com/po5/thumbfast/raw/master/thumbfast.lua
```

## Credits

- The main script is based on [mpv-osc-modern](https://github.com/maoiscat/mpv-osc-modern) and
  mpv's [`osc.lua`](https://github.com/mpv-player/mpv/blob/master/player/lua/osc.lua).
- `svgtoluapath.py` is based on [mpv-osc-tethys](https://github.com/Zren/mpv-osc-tethys).
- Icons are based on [material-design-icons](https://github.com/google/material-design-icons).
