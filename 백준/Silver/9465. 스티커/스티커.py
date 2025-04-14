import sys

input = sys.stdin.readline

def calc(stickers, n):
    for i in range(1, n):
        stickers[0][i] = max(stickers[0][i] + stickers[1][i - 1], stickers[0][i - 1])
        stickers[1][i] = max(stickers[1][i] + stickers[0][i - 1], stickers[1][i - 1])


t = int(input())
for _ in range(t):
    n = int(input())
    stickers = []
    stickers.append(list(map(int, input().split())))
    stickers.append(list(map(int, input().split())))
    calc(stickers, n)
    print(max(stickers[0][n - 1], stickers[1][n - 1]))