import sys
input = sys.stdin.readline

n = int(input())
b = [*map(int, input().split())]
a = []
try:
    i = max([i for i in b if i % 3 != 0])
    a.append(i)
    b.remove(i)
    for _ in range(n - 1):
        if i // 2 in b:
            i //= 2
            a.append(i)
            b.remove(i)
        elif i * 3 in b:
            i *= 3
            a.append(i)
            b.remove(i)
    print(*reversed(a))
except:
    i = max(b)
    temp = i
    for _ in range(n - 1):
        if temp // 2 in b:
            temp //= 2
            a.append(temp)
            b.remove(temp)
        elif temp * 3 in b:
            temp *= 3
            a.append(temp)
            b.remove(temp)
    a = [*reversed(a)]
    a.append(i)
    b.remove(i)
    for _ in range(n - 1):
        if i * 2 in b:
            i *= 2
            a.append(i)
            b.remove(i)
        elif i // 3 in b:
            i //= 3
            a.append(i)
            b.remove(i)
    print(*a)