n = [1, 1, 2, 2, 2, 8]
i = [*map(int, input().split())]
print(*[n[j] - i[j] for j in range(6)], sep= ' ')