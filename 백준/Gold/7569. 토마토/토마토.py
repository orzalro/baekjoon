import sys

input = sys.stdin.readline

m, n, h = map(int, input().split())

arr = [[0] * n for _ in range(h)]
tomato = []

for i in range(h):
    for j in range(n):
        row = list(map(int, input().split()))
        arr[i][j] = row
        count = 0
        while True:
            try:
                temp = row.index(1)
                count += temp
                row = row[temp + 1:]
                tomato.append([i, j, count, 0])
                count += 1
            except ValueError:
                break

total = 0
for y in arr:
    for x in y:
        total += sum(x)
empty_count = total - len(tomato)

def bfs(q):
    answer = 0
    next_q = []
    while len(q) != 0:
        for item in q:
            z, y, x, count = item
            if x + 1 < m and arr[z][y][x + 1] == 0:
                arr[z][y][x + 1] = 1
                next_q.append([z, y, x + 1, count + 1])
            if x - 1 >= 0 and arr[z][y][x - 1] == 0:
                arr[z][y][x - 1] = 1
                next_q.append([z, y, x - 1, count + 1])
            if y + 1 < n and arr[z][y + 1][x] == 0:
                arr[z][y + 1][x] = 1
                next_q.append([z, y + 1, x, count + 1])
            if y - 1 >= 0 and arr[z][y - 1][x] == 0:
                arr[z][y - 1][x] = 1
                next_q.append([z, y - 1, x, count + 1])
            if z + 1 < h and arr[z + 1][y][x] == 0:
                arr[z + 1][y][x] = 1
                next_q.append([z + 1, y, x, count + 1])
            if z - 1 >= 0 and arr[z - 1][y][x] == 0:
                arr[z - 1][y][x] = 1
                next_q.append([z - 1, y, x, count + 1])
            if count > answer:
                answer = count
        q = next_q
        next_q = []

    return answer

answer = bfs(tomato)

total = 0
for y in arr:
    for x in y:
        total += sum(x)

if total != m * n * h + empty_count * 2:
    print(-1)
else:
    print(answer)