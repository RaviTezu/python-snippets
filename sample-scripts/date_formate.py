#!/usr/bin/python
month=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
ending=['st','nd','rd']+17*['th']+['st','nd','rd']+8*['th']
d=int(raw_input("Enter the day[1-31]: "))
if not 1 <= d <= 31:
    print "Enter a valid day"
    exit() 
m=int(raw_input("Enter the month[1-12]: "))
if not 1 <= m <= 12:
    print "Enter a valid month"
    exit()
y=str(raw_input("Enter the year: "))
d1=d-1
m1=m-1
end=ending[d1]
month=month[m1]
day=str(d)
print "Date: " +day +end +" "+month +","+ y
