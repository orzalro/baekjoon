n = input().strip()
d = {int(c):n.count(c) for c in dict.fromkeys(n)}
print(*[str(i) * d[i] if i in d else '' for i in range(9, -1, -1)], sep= '')