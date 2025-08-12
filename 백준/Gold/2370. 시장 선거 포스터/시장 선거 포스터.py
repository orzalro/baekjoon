import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
posters = []
coords = []

# 입력
for _ in range(n):
    l, r = map(int, input().split())
    posters.append((l, r))
    coords.append(l)
    coords.append(r)

# 좌표 압축
coords = sorted(set(coords))
idx = {v: i for i, v in enumerate(coords)}

# Union-Find (다음 미덮인 인덱스 찾기)
parent = list(range(len(coords) + 1))  # 마지막+1까지 필요

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    parent[find(x)] = find(y)

count = 0
# 뒤에서부터 포스터 덮기
for l, r in reversed(posters):
    l_i, r_i = idx[l], idx[r]
    cur = find(l_i)
    painted = False
    while cur <= r_i:
        painted = True
        union(cur, cur + 1)  # 현재 칸 덮고 다음 칸으로
        cur = find(cur)
    if painted:
        count += 1

print(count)
