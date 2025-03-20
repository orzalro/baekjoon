import sys

input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))


max_num = 0
left = 0
d = {}

for right in range(n):
    fruit = l[right]

    if fruit not in d:
        d[fruit] = 1
        while len(d) > 2:
            fruit = l[left]
            d[fruit] -= 1
            if d[fruit] == 0:
                del d[fruit]
            left += 1
    else:
        d[fruit] += 1
    
    max_num = max(max_num, sum(d.values()))

print(max_num)