import sys
input = sys.stdin.readline

l = [*map(int, input().split())]
new_l = []

i = 0
for size in range(7, 0, -1):
    if size != 7:
        new_l.append([*[100 - new_l[row][7 - size] for row in range(7 - size)], -1, *l[i:i + size]])
    else:
        new_l.append([-1, *l[i:i + size]])
    i += size
new_l.append([100 - new_l[row][7] for row in range(7)])
new_l = [[p / 100 for p in row] for row in new_l]

r1 = []
for i in range(4):
    left = new_l[i * 2][i * 2 + 1]
    right = new_l[i * 2 + 1][i * 2]
    r1.append(left)
    r1.append(right)

r2 = []
for i in range(4):
    if i % 2: j = i * 2 - 2
    else: j = i * 2 + 2
    left = r1[i * 2] * (r1[j] * new_l[i * 2][j] + r1[j + 1] * new_l[i * 2][j + 1])
    right = r1[i * 2 + 1] * (r1[j] * new_l[i * 2 + 1][j] + r1[j + 1] * new_l[i * 2 + 1][j + 1])
    r2.append(left)
    r2.append(right)

r3 = []
for i in range(8):
    if i < 4:
        result = r2[i] * sum([r2[j] * new_l[i][j] for j in range(4, 8)])
    else:
        result = r2[i] * sum([r2[j] * new_l[i][j] for j in range(0, 4)])
    r3.append(result)

print(*r3, sep=' ')