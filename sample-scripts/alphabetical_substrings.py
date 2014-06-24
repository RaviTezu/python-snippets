#!/usr/bin/python

#Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print Longest substring in alphabetical order is: beggh

s = raw_input("s :")
x = len(s)
temp = s[0]
subs = []
for i in xrange(x-1):
    if s[i] <= s[i+1]:
        temp = temp + s[i+1]
    else:
        subs.append(temp)
        temp = s[i+1]
if ''.join(subs) != s:
    subs.append(temp)
if len(subs) != 0:
    print "Longest substring in alphabetical order is: " + max(subs, key=len)
else:
    print "Longest substring in alphabetical order is: " + s
