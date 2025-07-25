import sys
input = sys.stdin.readline

match_count = {1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6, 0:6}

def func(a, b, c, n):
    total = 0
    for i in [a, b, c]:
        total += match_count[i // 10] + match_count[i % 10]
    if total == n and a + b == c: return True
    else: return False

def calc(n):
    for a in range(0, 99):
        for b in range(0, 99):
            for c in range(0, 99):
                if func(a, b, c, n):
                    return f'{a:02d}+{b:02d}={c:02d}'
    return 'impossible'

n = int(input()) - 4
print(calc(n))