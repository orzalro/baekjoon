import sys

t = int(sys.stdin.readline().strip())

p = []
for i in range(14):
    p.append(i + 1)

list = []
list.append(p)

def calc(k, n):
    if k <= len(list):
        return sum(list[k-1][:n])
    else:
        for i in range(len(list), k):
            p = []
            for j in range(14):
                p.append(sum(list[i - 1][:j + 1]))
            list.append(p)
        return calc(k, n)


for i in range(t):
    k = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    print(calc(k, n))