#!/usr/bin/python

def isIn(char, aStr):
    low = 1
    high = len(aStr)
    mid = (low+high)/2
    while mid < len(aStr)-1:
       print "low:", low
       print "high:", high
       mid = (low+high)/2
       bStr = ''.join(sorted(aStr))
       if char == bStr[mid]:
           return True
           break
       elif char < bStr[mid]:
           high = mid
       elif char > bStr[mid]:
           low = mid
    return False 
c = raw_input("char: ")
s = raw_input("String: ")
print isIn(c,s)
