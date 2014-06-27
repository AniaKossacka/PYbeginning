inputHours = raw_input("Enter Hours:")
hours = float(inputHours)

inputRate = raw_input ("Enter Rate:")
rate = float (inputRate)
print rate, hours

if hours <= 40:
    pay = rate * hours
if hours > 40:
    pay = rate * 40 + (hours-40)* (1.5*rate)

print pay