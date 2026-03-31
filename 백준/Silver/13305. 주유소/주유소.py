import sys
input = sys.stdin.readline

n = int(input())
lengths = list(map(int, input().split()))
prices = list(map(int, input().split()))

answer = 0
i = 0
price = prices[i]

while i < n - 1:
    answer += lengths[i] * price
    if price > prices[i + 1]:
        price = prices[i + 1]
    i += 1

print(answer)