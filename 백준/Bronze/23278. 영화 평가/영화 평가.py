import sys
input = sys.stdin.readline

n, l, h = map(int, input().split())
scores = map(int, input().split())
if h:
    scores = sorted(scores)[l:-h]
else:
    scores = sorted(scores)[l:]
score = sum(scores) / (n - l - h)
print(score)