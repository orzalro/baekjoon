import sys
from collections import deque
input = sys.stdin.readline

def move():
    x, y = snake[0]
    nx = x + dx[snake_dir]
    ny = y + dy[snake_dir]

    if 0 <= nx < n and 0 <= ny < n:
        if board[ny][nx] == 0: # 빈칸일시
            snake.appendleft([nx, ny])
            board[ny][nx] = 2
            tx, ty = snake.pop()
            board[ty][tx] = 0
            return 1
        elif board[ny][nx] == 1: # 사과일시
            snake.appendleft([nx, ny])
            board[ny][nx] = 2
            return 1
    
    return 0

n = int(input())
board = [[0] * n for _ in range(n)]
board[0][0] = 2
snake = deque([[0, 0]])
snake_dir = 0 # 동남서북
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
t = 0

k = int(input())
for _ in range(k):
    y, x = map(int, input().split())
    board[y - 1][x - 1] = 1

l = int(input())
for _ in range(l):
    x, c = input().split()
    while t < int(x):
        if move():
            t += 1
        else:
            print(t + 1)
            exit()
    if c == 'L':
        snake_dir = snake_dir - 1 if snake_dir > 0 else 3
    else:
        snake_dir = snake_dir + 1 if snake_dir < 3 else 0

while True:
    if move():
        t += 1
    else:
        print(t + 1)
        break