#!/usr/bin/python
#It is a good practice to use print_funtion,
from __future__ import print_function

def horizon():
    """ Prints a Horizontal line!"""
    print("==========================================================================")

def list_comp():
    """ This snippet shows you, how to use List Comprehensions and there are similar to set comprehensions but with a {} braces"""
    print("\nLIST COMPREHENSIONS: ")
    org = [1, 2, 3, 4, 5]
    #Example1 
    horizon()
    print("Example-1: List comprehension without a condition \norg = [1, 2, 3, 4, 5] and ex1 = [i*i for i in org]")
    ex1 = [i*i for i in org]
    print("ex1 = " + str(ex1)+ "\n")
    #Example2
    print("Example-2:  List comprehension with a conition \norg = [1, 2, 3, 4, 5] and ex2 = [i*i for i in org if i%2!=0]")  
    ex2 = [i*i for i in org if i%2!=0]
    print("ex2 = " + str(ex2)+ "\n")
    print("Example-3:  List comprehension with a method \norg = ['A', 'B', 'C', 'D', 'E'] and ex3 = [i.lower() for i in org]")
    org1 =  ['A', 'B', 'C', 'D', 'E']
    ex3 = [i.lower() for i in org1 ]
    print("ex3 = " + str(ex3))
    horizon()
    #There is no tuple comprehension, however you can use a generator to do so. tuple(x**2 for x in tupe) would do the same!

def dict_comp():
    """ This snippet shows you, how to use dictionary Comprehention"""
    print("\nDICTIONARY COMPRESHENSIONS: ")
    org = {'a':1, 'b':2, 'c':3, 'd':4}
    #Example1
    horizon()
    print("Example-1: Dict comprehension without a condition \norg = {'a':1, 'b':2, 'c':3, 'd':4} and ex1 = {k:v*v for k,v in org.iteritems()}")
    ex1 = {k:v*v for k,v in org.iteritems()}
    print("ex1: "+ str(ex1)+"\n")
    print("Example-2: Dict comprehension with a condition \norg = {'a':1, 'b':2, 'c':3, 'd':4} and ex2 = {k:v*v for k,v in org.iteritems() if v%2!=0}")
    ex2 = {k:v*v for k,v in org.iteritems() if v%2!=0}
    print("ex2: "+ str(ex2))
    horizon()

if __name__ == "__main__":
    list_comp()
    dict_comp()
