import sys
input = sys.stdin.readline

def calc(n):
    floor = 0
    n1 = n
    while n1 != 1:
        n1 = n1 // 2
        floor += 1
    room = n - 2 ** floor + 1
    floor += 1
    print(f'{floor}{room:018}')

t = int(input())
for i in range(t):
    n = int(input())
    while n != 0:
        calc(n)
        n = n // 2