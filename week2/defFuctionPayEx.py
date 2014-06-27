""" parameters of the function correspond to:
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

