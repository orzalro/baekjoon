import sys
input = sys.stdin.readline

n, b, a = map(int, input().split())
p = [*map(lambda x: int(x) // 2, input().split())]
p.append(0)
p.sort()

for i in range(1, n):
    p[i + 1] += p[i]

if a:
    flag = 1
    for i in range(a):
        answer = i
        if p[i] > b:
            answer -= 1
            flag = 0
            break
    if flag:
        for i in range(a, n + 1):
            answer = i
            if p[i] + p[i - a] > b:
                answer -= 1
                break
else:
    for i in range(1, n + 1):
        answer = i
        if p[i] * 2 > b:
            answer -= 1
            break
print(answer)