#!/usr/bin/python

exts = open("extensions.conf", "r")
for line in exts:
    if "internalq-calls" in line and not line.startswith(';'):
        print "This is good line:", line,
