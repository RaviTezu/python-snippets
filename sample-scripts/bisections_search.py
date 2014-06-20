#!/usr/bin/python

print "Please think of a number between 0 and 100!"
start = 0
end   = 100
mid   = (start+end)/2
ip    = ""
while ip!= "c":
    print "Is your secret number " + str(mid) + "?"
    ip = raw_input("""Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low.  Enter 'c' to indicate I guessed correctly.""")
    if ip == "l":
       start = mid
    elif ip == "h":
       end   = mid
    elif ip == "c":
       print "Game over. Your secret number was: "+str(mid)
       break
    else:
       print "Sorry, I did not understand your input."
    
    mid = (start+end)/2
