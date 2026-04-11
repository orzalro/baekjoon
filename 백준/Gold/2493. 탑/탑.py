import sys
input = sys.stdin.readline

n = int(input())
towers = list(map(int, input().split()))

def calc():
    stack = []
    answer = [0] * n
    for i in range(1, n + 1):
        tower = towers[-i]
        while stack:
            j, h = stack[-1]
            if h <= tower:
                stack.pop()
                answer[-j] = n - i + 1
            else:
                break
        stack.append([i, tower])
    return answer

print(*calc())