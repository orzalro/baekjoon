import sys
input = sys.stdin.readline

def calc(n, k):
    a_total, b_total = k, k
    for _ in range(n):
        a, b = map(int, input().split())
        a_total -= a
        b_total -= b
        if a_total <= 0 and b_total <= 0:
            return 1
        elif a_total - 0.5 * a <= 0 and b_total > 0:
            return 1
        elif b_total <= 0:
            return -1
        elif any([a_total <= b_total - 50, a_total - 0.5 * a <= b_total - 50]):
            return 1
    return 0

n, k = map(int, input().split())
print(calc(n, k))
exit(0)