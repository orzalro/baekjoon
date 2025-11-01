import sys
input = sys.stdin.readline

n = int(input())
a = [*map(int, input().split())]
b = [*map(int, input().split())]

a.sort(reverse=True)
b.sort()
print(sum([a[i] * b[i] for i in range(n)]))