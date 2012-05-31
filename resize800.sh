#!/bin/bash
# resizes all jpegs suitable for web use. DESTRUCTIVE. MAKE COPIES.
# TODO: make non-destructive

for i in `ls *.jpg`;
do
convert $i -resize 800×600 $i
done
