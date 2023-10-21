#!/usr/bin/env python3

# Based on:
# https://github.com/Zren/mpv-osc-tethys/blob/master/icons/svgtohtmltoluapath.py

import argparse
import re
import subprocess
import sys
from pathlib import Path

ICONS_DIR = Path("icons")

N = r"(-?\d+\.?\d*)"  # int or float pattern
F = r"(-?\d+\.\d+)"  # float pattern

CANVAS = re.compile(rf"    <canvas id='canvas' width='{N}' height='{N}'></canvas>")
TRANSFORM = re.compile(r"\tctx\.transform\(.+")
MOVE_TO = re.compile(rf"\tctx\.moveTo\({F}, {F}\);")
LINE_TO = re.compile(rf"\tctx\.lineTo\({F}, {F}\);")
BEZIER_CURVE_TO = re.compile(rf"\tctx\.bezierCurveTo\({F}, {F}, {F}, {F}, {F}, {F}\);")


def convert_to_html_file(svg_file: Path) -> Path:
    html_file = svg_file.with_suffix(".html")
    subprocess.run(["inkscape", svg_file, "-o", html_file], check=True)
    return html_file


def clean_num(num: str) -> str:
    return num.rstrip("0").rstrip(".")


def generate_lua_path(html_file: Path) -> str:
    path = []
    with html_file.open("r") as f:
        for line in f.readlines():
            line = line.rstrip()
            # print(line)

            m = CANVAS.match(line)
            if m:
                # MPV's ASS alignment centering crops the path itself.
                # For the path to retain position in the SVG viewbox,
                # we need to "move" to the corners of the viewbox.
                cmd = "m 0 0"  # Top Left
                path.append(cmd)
                width = clean_num(m.group(1))
                height = clean_num(m.group(2))
                cmd = f"m {width} {height}"  # Bottom Right
                # print("size", cmd)
                path.append(cmd)
                continue

            m = TRANSFORM.match(line)
            if m:
                print(f"Error: Cannot parse ctx.transform(): '{html_file}'")
                print("Please ungroup path to remove transormation")
                sys.exit(1)

            m = MOVE_TO.match(line)
            if m:
                x = clean_num(m.group(1))
                y = clean_num(m.group(2))
                cmd = f"m {x} {y}"
                # print("moveTo", cmd)
                path.append(cmd)
                continue

            m = LINE_TO.match(line)
            if m:
                x = clean_num(m.group(1))
                y = clean_num(m.group(2))
                cmd = f"l {x} {y}"
                # print("lineTo", cmd)
                path.append(cmd)
                continue

            m = BEZIER_CURVE_TO.match(line)
            if m:
                cp1x = clean_num(m.group(1))
                cp1y = clean_num(m.group(2))
                cp2x = clean_num(m.group(3))
                cp2y = clean_num(m.group(4))
                x = clean_num(m.group(5))
                y = clean_num(m.group(6))
                cmd = f"b {cp1x} {cp1y} {cp2x} {cp2y} {x} {y}"
                # print("bezierCurveTo", cmd)
                path.append(cmd)
                continue

    return str(" ".join(path))


def print_lua_path(svg_file: Path) -> None:
    if not svg_file.is_file():
        print(f"Error: No such file: '{svg_file}'")
        sys.exit(1)

    name = svg_file.stem
    html_file = convert_to_html_file(svg_file)
    lua_path = generate_lua_path(html_file)
    print(rf'    {name} = "{{\\p1}}{lua_path}{{\\p0}}",')
    html_file.unlink()


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert SVG to Lua path and print.")
    parser.add_argument(
        "svg_files", metavar="SVG_FILE", type=Path, nargs="*", help="SVG icon file"
    )
    args = parser.parse_args()

    svg_files = args.svg_files if args.svg_files else sorted(ICONS_DIR.glob("*.svg"))

    print("local icons = {")

    for svg_file in svg_files:
        print_lua_path(svg_file)

    print("}")


if __name__ == "__main__":
    main()
