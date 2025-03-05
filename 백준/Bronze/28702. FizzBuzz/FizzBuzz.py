import sys

first = sys.stdin.readline().strip()
second = sys.stdin.readline().strip()
third = sys.stdin.readline().strip()

if first == 'Fizz':
    if second == 'Buzz' or third == 'Buzz':
        print('Fizz')
    else:
        if (int(third) + 1) % 5 == 0:
            print('FizzBuzz')
        else:
            print('Fizz')
    
elif first == 'Buzz':
    if second == 'Fizz':
        print(int(third) + 1)
    elif third == 'Fizz':
        print(int(second) + 2)
elif first == 'FizzBuzz':
    print('Fizz')
else:
    if (int(first) + 3) % 5 == 0:
        print('Buzz')
    else:
        print(int(first) + 3)