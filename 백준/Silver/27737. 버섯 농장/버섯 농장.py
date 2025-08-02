import sys
input = sys.stdin.readline

def bfs(farm, x, y, n, m, k):
    q = [[x, y]]
    farm[x][y] = 1
    m -= 1
    k_temp = k
    new_q = []
    while q:
        if k_temp == 0:
            if m:
                k_temp += k
                m -= 1
            else:
                return -1
        x, y = q.pop()
        k_temp -= 1
        if x + 1 < n and farm[x + 1][y] == 0:
            farm[x + 1][y] = 1
            new_q.append([x + 1, y])
        if y + 1 < n and farm[x][y + 1] == 0:
            farm[x][y + 1] = 1
            new_q.append([x, y + 1])
        if x > 0 and farm[x - 1][y] == 0:
            farm[x - 1][y] = 1
            new_q.append([x - 1, y])
        if y > 0 and farm[x][y - 1] == 0:
            farm[x][y - 1] = 1
            new_q.append([x, y - 1])
        if len(q) == 0:
            q = new_q
            new_q = []
    return m


n, m, k = map(int, input().split())
farm = [list(map(int, input().split())) for _ in range(n)]
m_temp = m
for i in range(n):
    for j in range(n):
        if farm[i][j] == 0:
            m_temp = bfs(farm, i, j, n, m_temp, k)
        if m_temp == -1:
            print('IMPOSSIBLE')
            exit(0)

if m_temp != m:
    print('POSSIBLE', m_temp, sep='\n')
else:
    print('IMPOSSIBLE')