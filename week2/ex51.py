""" Exercise: Write a program that repeatedly prompts a user 
for integer numbers until the user enters 'done'.
Once 'done' is entered, print out the largest and smallest
of the numbers. If the user enters anything other than 
a valid number catch it with a try/except and 
put out an appropriate message and ignore the number."""

largest = None
smallest = None
while True:
    input = raw_input("Enter a number: ")
    if input == "done" : break
    if len(input) < 1 : break
    try: number = int (input)

    except:
        print 'Invalid input'
        continue


    if number > largest: largest = number
    if smallest is None: smallest = number
    elif number < smallest: smallest = number

print "Maximum is", largest
print "Minimum is", smallest