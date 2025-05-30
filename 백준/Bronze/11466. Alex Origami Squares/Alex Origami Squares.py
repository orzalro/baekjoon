import sys
input = sys.stdin.readline


h, w = map(int, input().split())
answer = 0
if h / 3 < w:
    answer = max(answer, h / 3)
else:
    answer = max(answer, w)
if w / 3 < h:
    answer = max(answer, w / 3)
else:
    answer = max(answer, h)
if h / 2 <= w / 2:
    answer = max(answer, h / 2)
if w / 2 <= h / 2:
    answer = max(answer, w / 2)

print(answer)