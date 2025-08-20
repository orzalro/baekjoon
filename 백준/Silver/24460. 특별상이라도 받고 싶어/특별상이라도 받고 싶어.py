import sys
input = sys.stdin.readline

def calc(l):
    length = len(l)
    if length > 2:
        temp = []
        l1 = [row[length // 2:] for row in l[:length // 2]]
        l2 = [row[:length // 2] for row in l[:length // 2]]
        l3 = [row[:length // 2] for row in l[length // 2:]]
        l4 = [row[length // 2:] for row in l[length // 2:]]
        temp.append([calc(l2), calc(l1)])
        temp.append([calc(l3), calc(l4)])
        return calc(temp)
    else:
        if length == 1:
            return l[0][0]
        return sorted([i for row in l for i in row])[1]

n = int(input())
l = [[*map(int, input().split())] for _ in range(n)]
print(calc(l))