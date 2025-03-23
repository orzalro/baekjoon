import sys

input = sys.stdin.readline

n = int(input())
s_len = int(input())
s = input().strip()
pn = 'IO' * n + 'I'

i = 0
count = 0

while True:
    try:
        i = i + s[i:].index(pn) + 1
        count += 1
    except ValueError:
        print(count)
        break