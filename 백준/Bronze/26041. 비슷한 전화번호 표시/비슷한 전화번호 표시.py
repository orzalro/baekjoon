import sys
input = sys.stdin.readline

a = list(input().split())
b = input().strip()

count = 0
for s in a:
    if len(s) != len(b) and s.startswith(b):
        count += 1
print(count)