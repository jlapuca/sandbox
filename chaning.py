__author__ = 'vspir'

string = "this is a long-long-very-long string"

print string,
print type(string)

print string.split(" "),
print type(string.split(" "))

print string.split(" ")[3],
print type(string.split(" ")[3])

print string.split(" ")[3].split('-'),
print type(string.split(" ")[3].split('-'))

print string.split(" ")[3].split('-')[2],
print type(string.split(" ")[3].split('-')[2])