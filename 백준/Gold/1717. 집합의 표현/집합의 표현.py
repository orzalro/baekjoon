import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = list(range(n + 1))

def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)

    if y_root < x_root:
        parent[y_root] = x_root
    else:
        parent[x_root] = y_root

result = []
for _ in range(m):
    o, a, b = map(int, input().split())
    if o:
        if find(a) == find(b):
            result.append('YES')
        else:
            result.append('NO')
    else:
        union(a, b)

print('\n'.join(result))