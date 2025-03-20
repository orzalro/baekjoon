import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n, m = map(int, input().split())
campus = []
i_index = []

for i in range(n):
    a = input().strip()
    if len(i_index) < 1:
        if 'I' in a: i_index.append([i, a.index('I')])
    campus.append([item for item in a])

def dfs(y, x):
    count = 0
    if campus[y][x] == 'P': count += 1
    campus[y][x] = 'X'
    if x + 1 < m and campus[y][x + 1] != 'X':
        count += dfs(y, x + 1)
    if x - 1 >= 0 and campus[y][x - 1] != 'X':
        count += dfs(y, x - 1)
    if y + 1 < n and campus[y + 1][x] != 'X':
        count += dfs(y + 1, x)
    if y - 1 >= 0 and campus[y - 1][x] != 'X':
        count += dfs(y - 1, x)
    return count

answer = dfs(i_index[0][0], i_index[0][1])
print(answer if answer != 0 else 'TT')