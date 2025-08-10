import sys
input = sys.stdin.readline

def ncr(n, r):
    result = 1
    k = 1
    for i in range(n, n-r, -1):
        result *= i
    for i in range(r, 0,-1):
        k*=i
    return result//k

def calc(s, n, l:list):
    l = [l.count(i) for i in s]
    for i in l:
        if i == 0:
            return 0
    if sum(l) == n:
        return l[0] * l[1] * l[2]
    elif sum(l) == n * 3:
        return ncr(n, 3)
    else:
        if s[0] == s[1]:
            return ncr(l[0], 2) * l[2]
        elif s[0] == s[2]:
            return ncr(l[0], 2) * l[1]
        else:
            return ncr(l[1], 2) * l[0]


s = input().strip()
n = int(input())
l = []
for _ in range(n):
    temp = input()[0]
    if temp in s:
        l.append(temp)
print(calc(s, len(l), l))