import sys

n = int(sys.stdin.readline().strip())

def calc(n, temp=0):
    n5 = n // 5
    if n5 >= 5:
        return calc(n5, temp + n5)
    return n5 + temp

print(calc(n))