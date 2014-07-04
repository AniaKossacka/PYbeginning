# finding the largest number in a set
findingLargest = 0
for numberInSet in [9,41,12,3,74,15]:
    if numberInSet > findingLargest: findingLargest = numberInSet
print 'the largest number is:', findingLargest

# counting in a set
counter = 0
for numberInSet in [9,41,12,3,74,15]:
    counter = counter + 1
    #print in the loop
    print counter, numberInSet
# prints after the loop
print counter, numberInSet

# printing the running total
counter = 0
for numberInSet in [9,41,12,3,74,15]:
    counter = counter + numberInSet
    print counter, numberInSet
print 'the running total is:', counter

#finding the average
count = 0
sum = 0
for numberInSet in [9,41,12,3,74,15]:
    count = count + 1
    sum = sum + numberInSet
    print count, sum, numberInSet
print 'the average is:', float(sum)/count

# finding a number larger than 20
for numberInSet in [9,41,12,3,74,15]:
    if numberInSet > 20: print numberInSet

# using Boolean variables: is there a number 3 in the list
# found variable is sticky
found = False
for numberInSet in [9,41,12,3,74,15]:
    if numberInSet == 3: found = True
    print found, numberInSet

# makes more sense to add 'break' once the 3 is found
for numberInSet in [9,41,12,3,74,15]:
    if numberInSet == 3: found = True
    if numberInSet == 3: print found, numberInSet
    if numberInSet == 3: break

# finding the smallest number in a set
findingSmallest = findingLargest
for numberInSet in [9,41,12,3,74,15]:
    if numberInSet < findingSmallest: findingSmallest = numberInSet
print 'the smallest number is:', findingSmallest

