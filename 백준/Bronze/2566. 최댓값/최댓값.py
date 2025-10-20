import sys
input = sys.stdin.readline

answer = [-1]
for i in range(9):
    row = [*map(int, input().split())]
    max_num = max(row)
    if max_num > answer[0]:
        answer = [max_num, i + 1, row.index(max_num) + 1]

print(answer[0])
print(*answer[1:])