import random

def check1():
    return random.randrange(1,11)

def check2():
    random.seed(2)
    return random.randrange(1,11)

print "Without random.seed(0)"
for i in range(1,11):
    print check1()

print "With random.seed(0)"
for i in range(1,11):
    print check2()
