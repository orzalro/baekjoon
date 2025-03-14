import sys


n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

l = []
for i in range(m):
    l.append(list(map(int, (sys.stdin.readline().split()))))

s = set()
s.add(1)


while True:
    flag = 0
    for i in range(len(l)):
        a, b = l[i][0], l[i][1]
        if a in s or b in s:
            flag = 1
            s.add(a)
            s.add(b)
            l.pop(i)
            break
    if flag == 0:
        break

print(len(s) - 1)