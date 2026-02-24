import sys
input = sys.stdin.readline

def bfs(h, w, m):
    q = [[h, w]]
    next_q = []

    while q:
        for h, w in q:
            for i in range(max(0, h - 1), min(len(m), h + 2)):
                for j in range(max(0, w - 1), min(len(m[0]), w + 2)):
                    if m[i][j] == 1:
                        m[i][j] = 3
                        next_q.append([i, j])
        q = next_q
        next_q = []


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    
    m = [list(map(int, input().split())) for _ in range(h)]

    answer = 0
    for i in range(h):
        for j in range(w):
            if m[i][j] == 1:
                bfs(i, j, m)
                answer += 1
    print(answer)