import sys

input = sys.stdin.readline

n = int(input())
l = [[0] * n for _ in range(n)]
for y in range(n):
    string = list(map(int, (input().split())))
    for x in range(n):
        l[y][x] = string[x]

def calc(w, h, n):
    white, blue = 0, 0
    flag = 0

    for y in range(n):
        flag += sum(l[h + y][w:w + n])
    if flag == 0:
        return 1, 0
    elif flag == n ** 2:
        return 0, 1
    size = n // 2
    white1, blue1 = calc(w, h, size)
    white2, blue2 = calc(w + size, h, size)
    white3, blue3 = calc(w, h + size, size)
    white4, blue4 = calc(w + size, h + size, size)
    white += white1 + white2 + white3 + white4
    blue += blue1 + blue2 + blue3 + blue4

    return white, blue

white, blue = calc(0, 0, n)
print(white)
print(blue)