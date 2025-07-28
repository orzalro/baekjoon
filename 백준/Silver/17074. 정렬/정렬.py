import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, -float('inf'))
arr.append(float('inf'))

sorted_arr = sorted(arr)
if n == 2:
    print(n)
elif arr == sorted_arr:
    print(n)
else:
    count = 0
    for i in range(1, n + 1):
        if arr[i - 1] > arr[i]:
            count += 1
            pre = i - 1
            cur = i
        if count == 2:
            break
    if count > 1:
        print(0)
    else:
        print((arr[pre - 1] <= arr[cur]) + (arr[pre] <= arr[cur + 1]))