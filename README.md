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

1. Put `youtube-ui.lua` in your mpv `scripts` directory:

```sh
mkdir -p ~/.config/mpv/scripts
wget -P ~/.config/mpv/scripts https://github.com/eatsu/mpv-osc-youtube-ui/raw/main/youtube-ui.lua
```

2. Install the `Material-Design-Iconic-Font.ttf` font:

```sh
mkdir -p ~/.local/share/fonts
wget -P ~/.local/share/fonts https://github.com/eatsu/mpv-osc-youtube-ui/raw/main/Material-Design-Iconic-Font.ttf
```

3. Add `osc=no` to your `mpv.conf` file:

```sh
echo 'osc=no' >> ~/.config/mpv/mpv.conf
```

4. (optional) Put `thumbfast.lua` from [thumbfast](https://github.com/po5/thumbfast) in your mpv `scripts` directory:

```sh
wget -P ~/.config/mpv/scripts https://github.com/po5/thumbfast/raw/master/thumbfast.lua
```

## Credits

- The main script is based on [mpv-osc-modern](https://github.com/maoiscat/mpv-osc-modern) and
  mpv's [`osc.lua`](https://github.com/mpv-player/mpv/blob/master/player/lua/osc.lua).
- `svgtohtmltoluapath.py` is based on [mpv-osc-tethys](https://github.com/Zren/mpv-osc-tethys).
- Icons are based on [material-design-icons](https://github.com/google/material-design-icons).
