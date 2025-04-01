import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

def dslr(a, b):
    n = a
    q = deque()
    traceback = [[]] * 10000
    while n != b:
        d = n * 2 % 10000
        if not traceback[d]:
            traceback[d] = [n, 'D']
            q.append(d)

        s = n - 1 if n >= 1 else 9999
        if not traceback[s]:
            traceback[s] = [n, 'S']
            q.append(s)

        d1 = n // 1000
        d2 = n % 1000 // 100
        d3 = n % 100 // 10
        d4 = n % 10

        l = d2 * 1000 + d3 * 100 + d4 * 10 + d1
        if not traceback[l]:
            traceback[l] = [n, 'L']
            q.append(l)

        r = d4 * 1000 + d1 * 100 + d2 * 10 + d3
        if not traceback[r]:
            traceback[r] = [n, 'R']
            q.append(r)

        n = q.popleft()
    
    answer =''
    while b != a:
        answer = ''.join([traceback[b][1], answer])
        b = traceback[b][0]
        
    return answer

for i in range(t):
    a, b = map(int, input().split())
    print(dslr(a, b))

