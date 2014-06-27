#!/usr/bin/python

def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)

def semordnilap(str1, str2):
    '''
    str1: a string god
    str2: a string dog
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    
    if len(str1) == len (str2):
        if len(str1) == 1:
            return True
        elif str1[0] == str2[-1]:
           #print "comparing ", str1[0],"and",str2[-1]
           return semordnilap(str1[1:],str2[:-1])
    else:
        return False


s1 = raw_input("s1: ")
s2 = raw_input("s2: ")
print semordnilapWrapper(s1,s2)
