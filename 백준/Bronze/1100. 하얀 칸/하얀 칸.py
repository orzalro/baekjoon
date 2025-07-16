import sys
input = sys.stdin.readline

chess = []
count = 0
for i in range(8):
    chess.append(input().strip())

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            if chess[i][j] != '.':
                count += 1

print(count)