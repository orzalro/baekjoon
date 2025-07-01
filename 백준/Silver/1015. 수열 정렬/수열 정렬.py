import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

count = {}
sorted_a = sorted(a)
for i in a:
    if i in count:
        print(sorted_a.index(i) + count[i], end=' ')
        count[i] += 1
    else:
        print(sorted_a.index(i), end=' ')
        count[i] = 1