#!/usr/bin/python

#Assume s is a string of lower case characters.
#Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print - Number of times bob occurs is: 2

l = 0
count = 0
x = len(s)
for i in s:
    if i == "b" and l+1 < x and l+2 <x:
        if (s[l+1] == "o" and s[l+2]=="b"):
            count = count + 1
    l = l + 1
print "Number of times bob occurs is: "+str(count)
