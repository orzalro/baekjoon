import sys
input = sys.stdin.readline

s_l = [input().strip() for _ in range(5)]
answer = []
for i in range(15):
    for s in s_l:
        if len(s) > i:
            answer.append(s[i])
print(*answer, sep='')