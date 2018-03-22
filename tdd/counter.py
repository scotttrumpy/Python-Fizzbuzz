
def fizzbuzz(count):
    result = ''
    if (count % 15) == 0:
        result += 'fizzbuzz'        
    elif (count % 3) == 0:
        result += 'fizz'
    elif (count % 5) == 0:
        result += 'buzz'
    else:
        return count

    return result 

for n in range(1,101):
    fizzbuzz(n)

