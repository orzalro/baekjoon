import sys
input = sys.stdin.readline

s = input().strip()
n = int(input())
d = []
for i in range(n):
    d.append(input().strip()) 

flag = 0
for i in range(1, 27):
    decode_s = ''.join(map(lambda s: chr(s + i) if (s + i) < 123 else chr(s + i - 26), map(ord, s)))
    for word in d:
        if word in decode_s:
            print(decode_s)
            flag = 1
            break
    if flag == 1:
        break