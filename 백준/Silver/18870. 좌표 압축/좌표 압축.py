import sys

input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
d = {key:i for i, key in enumerate(sorted(set(l)))}

answer = [str(d[i]) for i in l]
print(' '.join(answer))