#!/usr/bin/python

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    d = {}
    for k,v in aDict.iteritems():
        d[k] = len(v)
    try:
        return max(d,key=d.get)
    except ValueError:
        return None
