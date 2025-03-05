import sys

n = int(sys.stdin.readline().strip())

list = [0] * 10001
for i in range(n):
    a = int(sys.stdin.readline().strip())
    list[a] += 1

for i in range(1, 10001):
    if list[i] != 0:
        for j in range(list[i]):
            print(i)