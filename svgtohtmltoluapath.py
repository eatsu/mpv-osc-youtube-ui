#!/usr/bin/env python3

# Based on:
# https://github.com/Zren/mpv-osc-tethys/blob/master/icons/svgtohtmltoluapath.py

import re
import subprocess
import os
import sys

canvasSizePattern = re.compile(r'    \<canvas id=\'canvas\' width=\'(-?\d+(\.\d+)?)\' height=\'(-?\d+(\.\d+)?)\'\>\<\/canvas\>')
transformPattern = re.compile(r'\tctx.transform\(.+')
moveToPattern = re.compile(r'\tctx.moveTo\((-?\d+\.\d+), (-?\d+\.\d+)\);')
lineToPattern = re.compile(r'\tctx.lineTo\((-?\d+\.\d+), (-?\d+\.\d+)\);')
curveToPattern = re.compile(r'\tctx.bezierCurveTo\((-?\d+\.\d+), (-?\d+\.\d+), (-?\d+\.\d+), (-?\d+\.\d+), (-?\d+\.\d+), (-?\d+\.\d+)\);')

def convertToCanvas(svgFilepath):
	htmlFilepath = svgFilepath.replace('.svg', '.html')
	subprocess.run([
		'inkscape',
		svgFilepath,
		'-o',
		htmlFilepath,
	])
	return htmlFilepath

def cleanNum(numstr):
	outstr = str(float(numstr))
	if outstr.endswith('.0'):
		outstr = outstr[:-2]
	return outstr

def generatePath(filepath):
	path = []
	with open(filepath, 'r') as fin:
		for line in fin.readlines():
			line = line.rstrip()
			# print(line)
			m = canvasSizePattern.match(line)
			if m:
				# MPV's ASS alignment centering crops the path itself.
				# For the path to retain position in the SVG viewbox,
				# we need to "move" to the corners of the viewbox.
				cmd = 'm 0 0' # Top Left
				path.append(cmd)
				w = cleanNum(m.group(1))
				h = cleanNum(m.group(3))
				cmd = 'm {} {}'.format(w, h) # Bottom Right
				# print('size', cmd)
				path.append(cmd)
				continue
			m = transformPattern.match(line)
			if m:
				print("[error] filepath:", filepath)
				print("Cannot parse ctx.transform()")
				print("Please ungroup path to remove transormation")
				sys.exit(1)
			m = moveToPattern.match(line)
			if m:
				x = cleanNum(m.group(1))
				y = cleanNum(m.group(2))
				cmd = 'm {} {}'.format(x, y)
				# print('moveTo', cmd)
				path.append(cmd)
				continue
			m = lineToPattern.match(line)
			if m:
				x = cleanNum(m.group(1))
				y = cleanNum(m.group(2))
				cmd = 'l {} {}'.format(x, y)
				# print('lineTo', cmd)
				path.append(cmd)
				continue
			m = curveToPattern.match(line)
			if m:
				x1 = cleanNum(m.group(1))
				y1 = cleanNum(m.group(2))
				x2 = cleanNum(m.group(3))
				y2 = cleanNum(m.group(4))
				x = cleanNum(m.group(5))
				y = cleanNum(m.group(6))
				cmd = 'b {} {} {} {} {} {}'.format(x1, y1, x2, y2, x, y)
				# print('curveTo', cmd)
				path.append(cmd)
				continue
	return ' '.join(path)

def printIcon(name, htmlFilepath):
	path = generatePath(htmlFilepath)
	print(r'    ' + name + r' = "{\\p1}' + path + r'{\\p0}",')

def genIconPath(name):
	svgFilepath = os.path.join('icons', name + '.svg')
	htmlFilepath = convertToCanvas(svgFilepath)
	printIcon(name, htmlFilepath)
	os.remove(htmlFilepath)

print('local icons = {')
genIconPath('play')
genIconPath('pause')
# genIconPath('close')
# genIconPath('minimize')
# genIconPath('maximize_enter')
# genIconPath('maximize_exit')
genIconPath('fs_enter')
genIconPath('fs_exit')
# genIconPath('ch_prev')
# genIconPath('ch_next')
genIconPath('info')
genIconPath('cy_audio')
genIconPath('cy_sub')
# genIconPath('pip_enter')
# genIconPath('pip_exit')
genIconPath('pl_prev')
genIconPath('pl_next')
genIconPath('skipback')
genIconPath('skipfrwd')
# genIconPath('speed')
genIconPath('volume_low')
genIconPath('volume_medium')
genIconPath('volume_high')
genIconPath('volume_over')
genIconPath('volume_mute')
print('}')
