import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == -1:
        break
    
    min_n = 0
    max_n = 0 
    if n % 2:
        for i in range(3, int(n ** 1/2), 2):
            if n % i == 0:
                min_n = i
                max_n = n // i
                break
    else:
        min_n = 2
        max_n = n // 2
    
    if min_n == 0:
        print(n, 'is NOT perfect.')
    else:
        l = [min_n]
        for j in range(min_n + 1, max_n):
            if n % j == 0:
                l.append(j)
        l.append(max_n)
        if sum(l) + 1 == n:
            print(n, end = ' = 1 + ')
            print(*l, sep = ' + ')
        else:
            print(n, 'is NOT perfect.')