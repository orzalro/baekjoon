import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

t = int(input().strip())

def calc(x, y, l, s):
    if [x, y] in s: return 0
    s.append([x, y])

    if [x, y + 1] in l and [x, y + 1] not in s:
        calc(x, y + 1, l, s)
    if [x, y - 1] in l and [x, y - 1] not in s:
        calc(x, y - 1, l, s)
    if [x - 1, y] in l and [x - 1, y] not in s:
        calc(x - 1, y, l, s)
    if [x + 1, y] in l and [x + 1, y] not in s:
        calc(x + 1, y, l, s)
    
    return 1

for testcase in range(t):
    cabage_list = []
    s = []
    area = 0

    m, n, k = map(int, input().split())
    for i in range(k):
        x, y = map(int, input().split())
        cabage_list.append([x, y])
    
    for i in cabage_list:
        x, y = i[0], i[1]
        area += calc(x, y, cabage_list, s)
    
    print(area)