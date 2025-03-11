import sys

n = int(sys.stdin.readline().strip())

list = []
for i in range(n):
    number = int(sys.stdin.readline().strip())
    list.append(number)

list.sort()
for i in list:
    print(i)