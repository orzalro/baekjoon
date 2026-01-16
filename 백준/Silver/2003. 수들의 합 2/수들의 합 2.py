import sys
input = sys.stdin.readline

n, m = map(int, input().split())

l = [0 for _ in range(n + 1)]
for i, num in enumerate(input().split(), 1):
    l[i] = l[i - 1] + int(num)
s = set(l)

answer = 0
for num in l:
    if num + m in s:
        answer += 1
print(answer)