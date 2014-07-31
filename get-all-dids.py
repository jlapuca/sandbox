#!/usr/bin/python
#-*- coding: utf-8 -*-

import ConfigParser

users = ConfigParser.ConfigParser()
users.read('users.conf')

print "%-20s\t%s\t%20s" % ('Name', 'ext', 'DIDS')


def get_username(section):
    if not section in users.sections():
        return
    try:
        return users.get(section, 'fullname')
    except ConfigParser.NoOptionError:
        return users.get(section, 'callerid').split('<')[0].strip()

phone_book = {
    ext: {
        'name': get_username(ext),
        'dids': [],
    } for ext in users.sections()
}

#print phone_book

exts = open("extensions.conf", "r")
for line in exts:
    if "internalq-calls" in line and not line.startswith(';'):
        fields = line.split(' ')[2].split(',')
        phone_book[fields[3]]['dids'].append(fields[0])
exts.close()

for ext in sorted(phone_book.keys()):
    print "%-20s\t%s\t%20s" % (phone_book[ext]['name'], ext, phone_book[ext]['dids'])