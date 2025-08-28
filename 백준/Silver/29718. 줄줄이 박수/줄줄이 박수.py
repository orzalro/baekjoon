import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = [[*map(int, input().split())] for _ in range(n)]
a = int(input())
result = 0
i = 0
new_l = [sum([row[i] for row in l]) for i in range(m)]
while True:
    result = max(result, sum(new_l[i : i + a]))
    i += 1
    if i + a > m:
        break
print(result)