import sys
input = sys.stdin.readline

n = int(input())
s = set()
for _ in range(n):
    name, command = input().split()
    if command == 'enter':
        s.add(name)
    else:
        s.discard(name)
print(*sorted(s, reverse=True), sep='\n')