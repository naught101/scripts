#!/usr/bin/python
# quick read of wiktionary

import urllib
import sys

sys.argv()

prefix="http://en.wiktionary.org/w/index.php?title="
suffix="&action=raw"

print(args)
url="".join([prefix,arg[1],suffix])

f = urllib.urlopen(url)
rawtext=f.read()
f.close()

print(text)

