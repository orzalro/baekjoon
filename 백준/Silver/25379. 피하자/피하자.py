import sys
input = sys.stdin.readline

n = int(input())
a = [*map(int, input().split())]
count = 0
left = [i for i, (num1, num2) in enumerate(zip(a, sorted(a, key=lambda x: x % 2)))if num1 != num2]
right = [i for i, (num1, num2) in enumerate(zip(a, sorted(a, key=lambda x: x % 2, reverse=True)))if num1 != num2]
if len(left) == 0:
    left = [0]
if len(right) == 0:
    right = [0]
print(min(max(left) - min(left), max(right) - min(right)))