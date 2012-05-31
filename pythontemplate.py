#!/usr/bin/python

print "hello world"
a,b =0,1
c,d = 0, 1.30496954493
while d < 10000 :
  if d>1 :
    print b, "\t", d
  a,b =b, a + b
  c,d = d,c+d
  ratio = float(b)/float(a)
exit
