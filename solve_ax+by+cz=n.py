#!/usr/bin/python

def McNuggets(n):
    """ This snippet can be used for finding the values of x,y,z in ax+by+cz=n where a,b,c and n are known."""
    if n == 0:
        return True
    for i in (6, 9, 20):
        if n >= i and McNuggets(n - i):
            return True
    return False 
