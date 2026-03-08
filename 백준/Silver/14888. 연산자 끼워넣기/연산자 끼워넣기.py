import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_answer = float('-inf')
min_answer = float('inf')

def calc(base, order):
    if order == n:
        global max_answer
        global min_answer
        max_answer = max(max_answer, base)
        min_answer = min(min_answer, base)
        return

    for i, op in enumerate(operators):
        if op == 0: continue
        if i == 0:
            operators[i] -= 1
            calc(base + numbers[order], order + 1)
            operators[i] += 1
        if i == 1:
            operators[i] -= 1
            calc(base - numbers[order], order + 1)
            operators[i] += 1
        if i == 2:
            operators[i] -= 1
            calc(base * numbers[order], order + 1)
            operators[i] += 1
        if i == 3:
            operators[i] -= 1
            if base >= 0:
                calc(base // numbers[order], order + 1)
            else:
                calc(-(abs(base) // numbers[order]), order + 1)
            operators[i] += 1

calc(numbers[0], 1)
print(max_answer, min_answer, sep='\n')