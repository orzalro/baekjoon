import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

t = int(input().strip())

def calc(x, y, l):
    l[x][y] = 0
    if y + 1 < len(l[0]) and l[x][y + 1] == 1:
        calc(x, y + 1, l)
    if y - 1 >= 0 and l[x][y - 1] == 1:
        calc(x, y - 1, l)
    if x - 1 >= 0 and l[x - 1][y] == 1:
        calc(x - 1, y, l)
    if x + 1 < len(l) and l[x + 1][y] == 1:
        calc(x + 1, y, l)
    

for testcase in range(t):
    m, n, k = map(int, input().split())
    cabage_list = [[0] * n for _ in range(m)]
    area = 0

    for i in range(k):
        x, y = map(int, input().split())
        cabage_list[x][y] = 1
    
    for y in range(n):
        for x in range(m):
            if cabage_list[x][y] == 1:
                calc(x, y, cabage_list)
                area += 1
    
    print(area)