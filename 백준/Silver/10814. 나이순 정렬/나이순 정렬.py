import sys

n = int(sys.stdin.readline().strip())

list = []
for i in range(n):
    age, name = map(str, (sys.stdin.readline().split()))
    list.append((age, name))

list.sort(key=lambda x: int(x[0]))

for i in list:
    print(i[0], i[1])