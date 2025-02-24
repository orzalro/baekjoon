import sys

n = int(sys.stdin.readline().strip())

numbers = []
for i in sys.stdin.readline().split():
    numbers.append(int(i))
print(min(numbers) ,max(numbers))