#!/usr/bin/python

n = int(raw_input("Enter the max. limit:"))

fib = [0,1]
while fib[-1] <= n:
    fib.append(fib[-2] + fib[-1])
print fib[:-1]
