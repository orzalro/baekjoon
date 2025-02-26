import sys

a = int(sys.stdin.readline().strip())
b = int(sys.stdin.readline().strip())
c = int(sys.stdin.readline().strip())

number = a * b * c
numbers = {'0': 0, '1' : 0, '2' : 0, '3' : 0, '4' : 0, '5' : 0, '6' : 0, '7' : 0, '8' : 0,  '9' : 0}
for i in str(number):
    numbers[i] += 1
for i in numbers:
    print(numbers[i])