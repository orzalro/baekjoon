import sys
input = sys.stdin.readline

n, k = map(int, input().split())
l = [0]
for i in map(int, input().split()):
    l.append(l[-1] + i)

answer = float('-inf')
for i in range(k, n + 1):
    num = l[i] - l[i - k]
    answer = max(answer, num)
print(answer)