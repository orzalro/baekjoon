import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = input().strip()

def calc(s, n, k):
    if (n - k) % 2 == 0:
        print(s[k-1:] + (s[:k-1])[::-1])
    else:
        print(s[k-1:] + s[:k-1])

calc(s, n, k)