import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
x = int(input())
answer = 0

numbers.sort()

l = 0
r = n - 1
while True:
    if l == r:
        break
    if numbers[l] + numbers[r] > x:
        r = max(0, r - 1)
    elif numbers[l] + numbers[r] < x:
        l = min(n - 1, l + 1)
    else:
        answer += 1
        l = min(n - 1, l + 1)
        r = min(n - 1, r + 1)
print(answer)