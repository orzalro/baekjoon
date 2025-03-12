import sys

n = int(sys.stdin.readline().strip())
nlist = list(map(int, (sys.stdin.readline().split())))
m = int(sys.stdin.readline().strip())
mlist = list(map(int, (sys.stdin.readline().split())))

list = [0] * 20000001
for i in nlist:
    list[i + 10000000] += 1

answer = []
for i in mlist:
    answer.append(list[i + 10000000])

print(' '.join(map(str, answer)))