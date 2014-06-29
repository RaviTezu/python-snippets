#!/usr/bin/python

def f(x):
    import math
    return 400*math.e**(math.log(0.5)/3.66 * x)

def radiationExposure(start, stop, step):
    
    height = []
    while start < stop:
        height.append(f(start))
        start +=step
    sums = [j*step for j in height]
    return sum(sums)

x = int(raw_input("start:"))
y = int(raw_input("stop:"))
z = float(raw_input("step:"))
print radiationExposure(x, y, z) 
    

