count = 0
while count < 100:
    if (count % 15) == 0:
        print ("fizzbuzz")
        count = count + 1
    elif (count % 3) == 0:
        print ("fizz")
        count = count + 1
    elif (count % 5) == 0:
        print ("buzz")
        count = count + 1
    else:
        print (count)
        count = count + 1