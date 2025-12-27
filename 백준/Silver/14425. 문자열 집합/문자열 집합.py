import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = set([input().strip() for _ in range(n)])

answer = 0
for _ in range(m):
    row = input().strip()
    if row in s:
        answer += 1
print(answer)