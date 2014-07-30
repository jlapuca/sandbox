#!/usr/bin/python
#-*- coding: utf-8 -*-

exts = open("extensions.conf", "r")

for line in exts:
    if "internalq-calls" in line and not line.startswith(';'):
        # для начала расписываю подробно, потом ужмем
        print "Got good line:", line,
        print "Start parsing..."

        # разделим строку на отдельные части там где были пробелы
        fields = line.split(' ')[2].split(',')
        print fields

        # откусываем заднюю часть
        #back = fields[2]

        # разделяем ее на части по запятым:
        #fields = back.split(',')
        #print fields

        # первый кусок целиком попал в 0-й элемент
        number = fields[0]+'\t'+fields[3]

        # второй кусок целиком попал в 3-й элемент
        #second_number = fields[3]

        #print "Find numbers:", first_number, second_number
        print "find numbers:", number

exts.close()