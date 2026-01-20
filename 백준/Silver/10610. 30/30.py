n = input().strip()
print(*sorted(n, reverse=True) if sum(map(int, n)) % 3 == 0 and '0' in n else [-1], sep='')