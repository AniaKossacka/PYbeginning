def computepay(h,r):
    if h <= 40: p = r * h
    if h > 40: p = r * 40 + (h-40)*(1.5*r)
    return p
    
try:
    inputHours = raw_input("Enter Hours:")
    hours = float(inputHours)

    inputRate = raw_input ("Enter Rate:")
    rate = float (inputRate)

except:
    print "Error, please enter numeric input"
    quit ()

pay = computepay(hours,rate)
print pay
