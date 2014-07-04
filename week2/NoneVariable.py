# finding the smallest number in a set using None variable
findingSmallest = None
for numberInSet in [9,41,12,3,74,15]:
    if findingSmallest is None: findingSmallest = numberInSet
    elif numberInSet < findingSmallest: findingSmallest = numberInSet
    print findingSmallest, numberInSet
print 'the smallest number is:', findingSmallest


