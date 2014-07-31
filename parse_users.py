#!/usr/bin/python
#-*- coding: utf-8 -*-

import ConfigParser

config = ConfigParser.ConfigParser()
config.read('users.conf')
print config.sections()
