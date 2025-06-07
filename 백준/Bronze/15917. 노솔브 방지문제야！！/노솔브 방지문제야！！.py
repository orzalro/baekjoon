import sys
input = sys.stdin.readline

q = int(input())
for i in range(q):
    a = int(input())
    while a % 2 == 0:
        a = a // 2
    print(1 if a == 1 else 0)