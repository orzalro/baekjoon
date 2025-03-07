import sys

n = sys.stdin.readline().strip()

s = set()

for i in range(int(n)):
    s.add(sys.stdin.readline().strip())

s = list(s)
s.sort()
s.sort(key=lambda x: len(x))
for i in s:
    print(i)