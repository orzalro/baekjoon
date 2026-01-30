import sys
input = sys.stdin.readline

n = int(input())

answer = 0
dp = [0]
for i in range(1, n - 1):
    dp.append(dp[-1] + i)
print(sum(dp))

print(3)