import sys

input = sys.stdin.readline

n = int(input())
s_len = int(input())
s = input().strip()
pn = 'IO' * n + 'I'
pn_len = 2 * n + 1

count = 0


while True:
    i = s.find(pn)
    if i == -1:
        break
    while s[i + pn_len:i + pn_len + 2] == 'OI':
        i += 2
        count += 1
    count += 1
    s = s[i + pn_len:]

print(count)