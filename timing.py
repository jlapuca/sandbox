__author__ = 'vspir'


def variant_1():
    exts = open("extensions.conf", "r")

    for line in exts:
        if "internalq-calls" in line and not line.startswith(';'):
            fields = line.split(' ')[2].split(',')
            #print "find numbers: %s\t%s" % (fields[0], fields[3])

    exts.close()


def variant_2():
    exts = open("extensions.conf", "r")

    for line in exts:
        if not line.startswith(';') and "internalq-calls" in line:
            fields = line.split(' ')[2].split(',')
            #print "find numbers: %s\t%s" % (fields[0], fields[3])

    exts.close()


import timeit

print 'What about lazy logic here?'
print timeit.timeit(stmt='variant_1()', setup='from __main__ import variant_1', number=100000)
print timeit.timeit(stmt='variant_2()', setup='from __main__ import variant_2', number=100000)