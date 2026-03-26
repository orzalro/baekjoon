import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

arr = [nums[0]]
for i in range(1, n):
    arr.append(arr[-1] + nums[i])

def calc():
    left = 0
    length = 0

    for _ in range(n):
        if arr[length] < s:
            length += 1
        else:
            break
    
    if length == n:
        return 0

    while True:
        if length == 0 or left + length > n - 1: break
        if arr[left + length] - arr[left] >= s:
            length -= 1
        left += 1

    return length + 1

print(calc())