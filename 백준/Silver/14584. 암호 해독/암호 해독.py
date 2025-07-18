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
    if any(w in decode_s for w in d): print(decode_s); break