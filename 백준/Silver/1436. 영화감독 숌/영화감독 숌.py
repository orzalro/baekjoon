import sys

n = int(sys.stdin.readline().strip())

count = 1
number = 666
while count != n:
    number += 1
    if '666' in str(number):
        count += 1
print(number)
