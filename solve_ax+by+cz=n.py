#!/usr/bin/python

def McNuggets(n):
    """ 6a+9b+20c = n"""
    if n == 0:
        return True
    for i in (6, 9, 20):
        if n >= i and McNuggets(n - i):
            return True
    return False 
