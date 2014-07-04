count = 0
total = 0

while True:
    input = raw_input('enter a number: ')
    #edge cases
    if input == 'done': break
    if len(input) < 1 : break # checks for an empty line
    
    try: number = float (input)
    except:
        print 'invalid input'
        continue
    count = count + 1
    total = total + number
    print number, total, count
    
print 'average:', total/count