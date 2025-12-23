a, b = map(int, input().split())
l = []
[l.extend([i] * i) for i in range(1, 50) if len(l) < b]
print(sum(l[a-1:b]))