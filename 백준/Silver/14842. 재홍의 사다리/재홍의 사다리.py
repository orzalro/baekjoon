import sys
input = sys.stdin.readline

w, h, n = map(int, input().split())

def f(x):
    return h / w * x
def g(x):
    return -h / w * x + h

s = 0
for i in range(1, n // 2 + 1):
    x = w / n * i
    s += abs(f(x) - g(x))

print(s * 2)