import sys
input = sys.stdin.readline

n = int(input())
pre = 0
num = 1
if n == 0:
    print(0)
else:
    for i in range(n - 1):
        num, pre = (num + pre) % 1000000007, num % 1000000007
    print(num)