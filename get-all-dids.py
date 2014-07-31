#!/usr/bin/python
#-*- coding: utf-8 -*-

import ConfigParser

exts = open("extensions.conf", "r")
users = ConfigParser.ConfigParser()
users.read('users.conf')

print "%-20s\t%s\t%20s" % ('Name', 'ext', 'DID')


def getUsername(section):
    if not section in users.sections():
        return
    try:
        return users.get(section, 'fullname')
    except ConfigParser.NoOptionError:
        return users.get(section, 'callerid').split('<')[0].strip()

for line in exts:
    if "internalq-calls" in line and not line.startswith(';'):
        fields = line.split(' ')[2].split(',')
        print "%-20s\t%s\t%20s" % (getUsername(fields[3]), fields[3], fields[0])

exts.close()
