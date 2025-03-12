import sys

k = int(sys.stdin.readline().strip())

list = []
for i in range(k):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        del list[-1]
    else:
        list.append(num)
print(sum(list))