import sys

numbers = []

for i in range(9):
    numbers.append(int(sys.stdin.readline().strip()))

max = max(numbers)
print(max)
print(numbers.index(max) + 1)