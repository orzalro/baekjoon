import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

heights = set()
[[heights.add(height) for height in row] for row in matrix]

def bfs(h, x, y):
    q = [[x, y]]
    new_q = []

    while q:
        for i, j in q:
            if j + 1 < n and matrix_temp[j + 1][i] > h:
                matrix_temp[j + 1][i] = h
                new_q.append([i, j + 1])
            if j > 0 and matrix_temp[j - 1][i] > h:
                matrix_temp[j - 1][i] = h
                new_q.append([i, j - 1])
            if i + 1 < n and matrix_temp[j][i + 1] > h:
                matrix_temp[j][i + 1] = h
                new_q.append([i + 1, j])
            if i > 0 and matrix_temp[j][i - 1] > h:
                matrix_temp[j][i - 1] = h
                new_q.append([i - 1, j])
        q = new_q
        new_q = []

max_safe_count = 1
for h in heights:
    safe_count = 0
    matrix_temp = [[height for height in row] for row in matrix]
    for y in range(n):
        for x in range(n):
            if matrix_temp[y][x] > h:
                bfs(h, x, y)
                safe_count += 1
    max_safe_count = max(max_safe_count, safe_count)

print(max_safe_count)