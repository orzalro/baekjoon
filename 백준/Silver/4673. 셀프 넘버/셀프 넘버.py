import sys
input = sys.stdin.readline

def calc(n):
    return n + n // 1000 + (n % 1000) // 100 + (n % 100) // 10 + n % 10
s = set()
for i in range(1, 10001):
    if i in s: continue
    print(i)
    while True:
        s.add(i)
        i = calc(i)
        if i in s or i > 10000:
            break