import sys

input = sys.stdin.readline

n, m = map(int, input().split())

l = list(map(int, input().split()))

min_h = max(l) - m
max_h = max(l)

l.sort()

left = 0
right = len(l) - 1
while min_h != max_h:
    while True:
        if l[left] == min_h:
            left += 1
            break
        elif l[left] > min_h:
            left, right = left // 2, left
            if left == right:
                break
        else:
            new_left = (left + right) // 2
            if left == new_left:
                left += 1
                break
            else: left = new_left
    right = len(l) - 1
    
    num = sum(l[left:right + 1]) - (right + 1 - left) * min_h
    if num == m:
        break
    elif num > m:
        new_min_h = (min_h + max_h) // 2
        if min_h == new_min_h: break
        else: min_h = new_min_h
    else:
        min_h, max_h = (min_h * 3 - max_h) // 2, min_h

print(min_h)