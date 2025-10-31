import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

def calc():
    if len(arr) == m:
        print(*arr)
        return
    for i in range(1, n + 1):
        arr.append(i)
        calc()
        arr.pop()

calc()
