#!/usr/bin/python
#-*- coding: utf-8 -*-

import ConfigParser

exts = open("extensions.conf", "r")
users = ConfigParser.ConfigParser()
users.read('users.conf')

print "%-20s\t%s\t%20s" % ('Name','ext', 'DID')

for line in exts:
    if "internalq-calls" in line and not line.startswith(';'):
        fields = line.split(' ')[2].split(',')
        user = users.get(fields[3], 'fullname')
        print "%-20s\t%s\t%20s" % (user, fields[3], fields[0])


exts.close()
