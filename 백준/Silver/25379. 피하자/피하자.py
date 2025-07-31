import sys
input = sys.stdin.readline

n = int(input())
a = [i % 2 for i in map(int, input().split())]

def calc(a, num):
    count = 0
    left = 0
    for i, n in enumerate(a):
        if n == num:
            count += i - left
            left += 1
    return count

print(min(calc(a, 0), calc(a, 1)))