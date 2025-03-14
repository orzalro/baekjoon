import sys


n = int(sys.stdin.readline().strip())
l = list(map(int,(sys.stdin.readline().split())))
l.sort()

sum = 0

for i in range(n):
    sum += l[i] * (n - i)

print(sum)