#!/bin/bash

#cvt -r 1680 1050 60
# 1680x1050 59.88 Hz (CVT 1.76MA-R) hsync: 64.67 kHz; pclk: 119.00 MHz
#Modeline "1680x1050R"  119.00  1680 1728 1760 1840  1050 1053 1059 1080 +hsync -vsync

xrandr --newmode "1680x1050N"  119.00  1680 1728 1760 1840  1050 1053 1059 1080 +hsync -vsync
xrandr --addmode VGA1 "1680x1050N"
xrandr --output VGA1 --mode "1680x1050N"
