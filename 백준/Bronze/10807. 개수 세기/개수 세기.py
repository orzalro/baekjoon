import sys
input = sys.stdin.readline

n = int(input().strip())
numbers = list(map(int, input().split()))
v = int(input().strip())
print(numbers.count(v))