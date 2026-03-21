import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = [input().strip() for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited_states = set()

def calc(x, y, visited):
    if (x, y, visited) in visited_states:
        return 0
    visited_states.add((x, y, visited))

    cnt = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < c and 0 <= ny < r:
            char = ord(board[ny][nx]) - 65

            if visited & (1 << char):
                continue

            cnt = max(cnt, calc(nx, ny, visited | (1 << char)))

    return cnt + 1

print(calc(0, 0, 1 << (ord(board[0][0]) - 65)))