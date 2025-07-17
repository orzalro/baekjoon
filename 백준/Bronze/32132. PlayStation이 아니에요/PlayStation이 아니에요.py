import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()

while True:
    s_len = len(s)
    s = s.replace('PS4', 'PS')
    s = s.replace('PS5', 'PS')
    if s_len == len(s):
        break

print(s)