import sys


number = int(sys.stdin.readline().strip())

for i in range(number):
    n, m = map(int, (sys.stdin.readline().split()))
    l = list(map(int, (sys.stdin.readline().split())))
    if n == 1:
        print(1)
        continue
    
    count = 1
    while len(l) != 0:
        flag = 0
        for i in range(l[0] + 1, 10):
            if i in l:
                flag = 1
                l.append(l.pop(0))
                break
        if flag == 0:
            if m == 0:
                print(count)
                break
            l.pop(0)
            count += 1
        m = m - 1 if m - 1 >= 0 else len(l) - 1