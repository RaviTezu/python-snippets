#!/usr/bin/python

def fact(num):
    if num == 1:
       return 1
    else:
        return num*fact(num-1)

n = int(raw_input("Enter a number: "))
f = fact(n)
print n,f

  
