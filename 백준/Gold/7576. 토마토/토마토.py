import sys

input = sys.stdin.readline

m, n = map(int, input().split())

arr = [[] for _ in range(n)]
tomato = []
empty_count = 0

for i in range(n):
    row = list(map(int, input().split()))
    arr[i] = row
    count = 0
    row2 = row
    while True:
        try:
            temp = row2.index(1)
            count += temp
            row2 = row2[temp + 1:]
            tomato.append([i, count, 0])
            count += 1
        except ValueError:
            break

total = 0
for x in arr:
    total += sum(x)
empty_count = total - len(tomato)

def bfs(q):
    answer = 0
    next_q = []
    ripe_count = len(q)
    while len(q) != 0:
        for item in q:
            y, x, count = item
            if x + 1 < m and arr[y][x + 1] == 0:
                arr[y][x + 1] = 1
                ripe_count += 1
                next_q.append([y, x + 1, count + 1])
            if x - 1 >= 0 and arr[y][x - 1] == 0:
                arr[y][x - 1] = 1
                ripe_count += 1
                next_q.append([y, x - 1, count + 1])
            if y + 1 < n and arr[y + 1][x] == 0:
                arr[y + 1][x] = 1
                ripe_count += 1
                next_q.append([y + 1, x, count + 1])
            if y - 1 >= 0 and arr[y - 1][x] == 0:
                arr[y - 1][x] = 1
                ripe_count += 1
                next_q.append([y - 1, x, count + 1])
            if count > answer:
                answer = count
        q = next_q
        next_q = []

    return answer, ripe_count

answer, ripe_count = bfs(tomato)

if m * n != ripe_count - empty_count:
    print(-1)
else:
    print(answer)