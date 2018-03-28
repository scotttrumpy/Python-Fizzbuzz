def fizzbuzz (count):

    if count % 15 == 0:
        return('Fizzbuzz')
    elif count % 3 == 0:
        return('Fizz')
    elif count % 5 == 0:
        return('Buzz')
    else:
        return count

def main():
    for count in range(1,101):
        print fizzbuzz(count)


if __name__=='__main__':
    main()

