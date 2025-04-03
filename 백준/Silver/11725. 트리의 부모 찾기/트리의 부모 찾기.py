import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)

def dfs(root):
    visited.add(root)
    for i in tree[root]:
        if i not in visited:
            parent[i - 1] = root
            dfs(i)

visited = set()
parent = [[]] * (n - 1)
dfs(0)
for i in parent:
    print(i + 1)