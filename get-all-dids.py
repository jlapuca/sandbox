#!/usr/bin/python
#-*- coding: utf-8 -*-

exts = open("extensions.conf", "r")

print "%20s\t%s" % ('DID', 'ext')

for line in exts:
    if "internalq-calls" in line and not line.startswith(';'):
        fields = line.split(' ')[2].split(',')
        print "%20s\t%s" % (fields[0], fields[3])

exts.close()