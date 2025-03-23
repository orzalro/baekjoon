import sys

input = sys.stdin.readline

n = int(input())
s_len = int(input())
s = input().strip()
pn = 'IO' * n + 'I'
pn_len = 2 * n + 1

i = 0
count = 0


while i < s_len - pn_len + 1:
    if s[i] == 'I':
        if s[i:i + pn_len] == pn:
            while s[i + pn_len:i + pn_len + 2] == 'OI':
                i += 2
                count += 1
            i += pn_len
            count += 1
        else:
            i += 1
    else:
        i += 1

print(count)