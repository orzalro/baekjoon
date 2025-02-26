import sys

s = sys.stdin.readline().strip()
d = dict()

for i in range(97, 123):
    d[chr(i)] = -1

for i in range(len(s)):
    c = s[i]
    if d[c] == -1:
        d[c] = i

for i in d:
    print(d[i], end=' ')