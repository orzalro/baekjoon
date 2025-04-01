import sys

input = sys.stdin.readline

n, m = map(int, (input().split()))

# 1부터 n까지의 수 중 m개씩 묶어서 오름차순 수열 만들기

def calc(start, end, m):
    result = []
    if m < 1:
        return
    else:
        for i in range(start, end + 1):
            temp = calc(i, end, m - 1)
            if temp is not None:
                for j in temp:
                    result.append([i, j])
            else: result.append(i)
        return result

def answer(result):
    if type(result) is int:
        print(result, end=' ')
    else:
        for i in range(len(result)):
            answer(result[i])

result = calc(1, n, m)
for i in range(len(result)):
    answer(result[i])
    print()