""" Exercise: Write a program to prompt the user
for hours and rate per hour using raw_input to compute
gross pay. Award time-and-a-half for the hourly rate for
all hours worked above 40 hours. Put the logic to do the
computation of time-and-a-half in a function called
computepay() anduse the function to do the computation.
The function should return a value. Use raw_input to
read a string and float() to convert the string to a number.

parameters of the function correspond to:
h - hours
r - rate
p - pay
in the main code"""

def computepay(h, r):
    print "in the function computepay", h, r
    if h <= 40: p = r * h
    elif h > 40: p = r * 40 + (h-40)* (1.5*r)
    print "finished with computepay", p
    return p

try:
    inputHours = raw_input("Enter Hours:")
    hours = float(inputHours)

    inputRate = raw_input ("Enter Rate:")
    rate = float (inputRate)

except:
    print "Error, please enter numeric input"
    quit ()

print "in the main code", hours, rate
pay = computepay(hours,rate)
print pay

