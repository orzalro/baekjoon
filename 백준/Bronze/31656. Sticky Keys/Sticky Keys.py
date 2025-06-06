import sys
input = sys.stdin.readline

s = input().rstrip()

while True:
    if len(s) == 0: break
    print(s[0], end='')
    s = s.lstrip(s[0])