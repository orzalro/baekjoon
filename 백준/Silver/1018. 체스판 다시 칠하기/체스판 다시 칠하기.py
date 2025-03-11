import sys

n, m = map(int, (sys.stdin.readline().split()))

list = [] * n
for i in range(n):
    list.append(sys.stdin.readline().strip())


repaint = 64
for row in range(n - 7):
    for col in range(m - 7):
        wstart = 0
        bstart = 0
        for i in range(8):
            for j in range(8):
                if list[row + i][col + j] == 'W':
                    if (i + j) % 2 == 0:
                        wstart += 1
                    else:
                        bstart += 1
                else:
                    if (i + j) % 2 == 0:
                        bstart += 1
                    else:
                        wstart += 1
        if repaint > min(wstart, bstart):
            repaint = min(wstart, bstart)
print(repaint)