import sys
input = sys.stdin.readline

def get_size(n):
    return (1 + n) * 2 * n

t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    max_start = get_size(n)
    min_start = get_size(n - k - 1) if n - k > 1 else 0
    print(max_start - min_start)