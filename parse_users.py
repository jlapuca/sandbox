#!/usr/bin/python
#-*- coding: utf-8 -*-

__author__ = 'vspir'

current_section = None

f = open('users.conf', 'r')

for line in f:
    if line.startswith('['):
        # написать код изменения current_section
        pass
    print current_section