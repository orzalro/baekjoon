import sys

n, k = map(int, (sys.stdin.readline().split()))
list = []

for i in range(n):
    list.append(i + 1)

answer = []
count = 0

while len(list) != 0:
    count += k-1
    while count >= len(list): count -= len(list)
    answer.append(list.pop(count))


print(f"<{', '.join(map(str, answer))}>")