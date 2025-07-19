import sys
input = sys.stdin.readline

n = int(input())
result = 1
for i in range(1, n, 2):
    result *= i
print(result % (10**9 + 7))