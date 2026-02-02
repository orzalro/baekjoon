import sys
input = sys.stdin.readline

while True:
    s = input().strip().lower()
    if s == '#': break
    print(sum([s.count(char) for char in ['a', 'e', 'i', 'o', 'u']]))