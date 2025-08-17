def calc(board, y, x):
    board[y][x] = 2
    for row in range(y - 1, y + 2):
        if row >= len(board) or y < 0: continue
        for col in range(x - 1, x + 2):
            if col >= len(board) or col < 0: continue
            if board[row][col] == 1: calc(board, row, col)
            else: board[row][col] = 2

def solution(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                calc(board, row, col)
    
    answer = 0
    for row in board:
        answer += sum(row)
    answer = len(board) ** 2 - answer // 2
    return answer