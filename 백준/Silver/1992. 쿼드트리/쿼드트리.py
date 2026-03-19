import sys
input = sys.stdin.readline

def calc(arr):
    if all([all(row) for row in arr]):
        print(1, end='')
    elif any([any(row) for row in arr]):
        l = len(arr)
        print('(', end='')
        calc([row[:l // 2] for row in arr[:l // 2]])
        calc([row[l // 2:] for row in arr[:l // 2]])
        calc([row[:l // 2] for row in arr[l // 2:]])
        calc([row[l // 2:] for row in arr[l // 2:]])
        print(')', end='')
    else:
        print(0, end='')

n = int(input())
arr = [list(map(int, input().strip())) for _ in range(n)]
calc(arr)