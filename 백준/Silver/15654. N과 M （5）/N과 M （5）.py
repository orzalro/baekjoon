import sys

input = sys.stdin.readline

n, m = map(int, (input().split()))
num = list(map(int, input().split()))

def calc(arr, m):
    result = []
    if m < 1:
        return
    else:
        for i in range(0, len(arr)):
            new_arr = arr[:i];new_arr.extend(arr[i + 1:])
            temp = calc(new_arr, m - 1)
            if temp is not None:
                for j in temp:
                    result.append([arr[i], j])
            else: result.append(arr[i])
        return result

def answer(result):
    if type(result) is int:
        print(result, end=' ')
    else:
        for i in range(len(result)):
            answer(result[i])

num.sort()
result = calc(num, m)
for i in range(len(result)):
    answer(result[i])
    print()