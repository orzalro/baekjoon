import sys
input = sys.stdin.readline

def combi(a, b):
    temp = 1
    for i in range(a, b, -1):
        temp *= i
    for i in range(a - b, 1, -1):
        temp //= i
    return temp

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(combi(m, n))