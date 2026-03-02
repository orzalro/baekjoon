import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = [i for i in range(1, n + 1)]
find = list(map(int, input().split()))

cur = 0
answer = 0
for num in find:
    i = numbers.index(num)
    answer += min(abs(cur - i), len(numbers) - cur + i if cur > i else len(numbers) - i + cur)
    cur = i
    numbers.pop(cur)


print(answer)