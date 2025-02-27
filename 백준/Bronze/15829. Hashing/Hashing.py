import sys

l = int(sys.stdin.readline().strip())
a = sys.stdin.readline().strip()

r = 31
s = 0

for i in range(l):
    s += (ord(a[i]) - 96) * r ** i
print(s)