import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

def dfs(pre, numbers, m):
    if m > 0:
        next_nums = numbers
        for n in numbers:
            cur = pre + [n]
            dfs(cur, next_nums, m - 1)
            next_nums = next_nums[1:]
    else:
        print(*pre)

dfs([], numbers, m)