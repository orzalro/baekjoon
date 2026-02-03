import sys
input = sys.stdin.readline

d = {i:sum(map(int, input().split())) for i in range(1, 6)}
sorted_d = sorted(d, key=lambda x: d[x], reverse=True)
print(sorted_d[0], d[sorted_d[0]])