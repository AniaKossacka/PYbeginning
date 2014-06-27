try:
    inputScore = raw_input("Enter Score:")
    score = float(inputScore)

except:
    print "Error, please enter numeric input"
    quit ()
    
if score >= 0.9: print "A"
elif score >= 0.8: print "B"
elif score >= 0.7: print "C"
elif score >= 0.6: print "D"
else: print "F"