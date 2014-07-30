#!/usr/bin/python2

exts = open("/home/lyakovleva/extensions.conf", "r")
for line in exts:
  if "internalq-calls" in line and ';' not in line:
    print "This is good line:", line,
