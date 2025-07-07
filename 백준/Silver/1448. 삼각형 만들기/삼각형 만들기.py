import sys
input = sys.stdin.readline

n = int(input())

l = []
for i in range(n):
    l.append(int(input()))

l.sort()
a, b, c = (l.pop() for _ in range(3))
while True:
    if a < b + c:
        print(a + b + c)
        break
    try:
        a, b, c = b, c, l.pop()
    except:
        print(-1)
        break