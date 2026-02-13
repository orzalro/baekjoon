s = input().strip()
print(*sorted([s[i:] for i in range(len(s))]), sep='\n')