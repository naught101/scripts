#!/bin/bash

xmodmap -e "clear lock"
xmodmap -e "keycode 0x42 = Escape"
xmodmap -e "keycode 0x09 = Multi_key"
