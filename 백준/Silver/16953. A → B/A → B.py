import sys

input = sys.stdin.readline

a, b = map(int, (input().split()))

def greedy(a, b):
    count = 1
    while a != b:
        if a > b: return -1
        if b % 10 == 1: b = b // 10
        elif b % 2 == 0: b = b // 2
        else: return -1
        count += 1
    return count

print(greedy(a, b))