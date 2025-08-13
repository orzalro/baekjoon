import sys
input = sys.stdin.readline

rh, rv, sh, sv = map(int, input().split())
n = int(input())
l = []
for i in range(n):
    l.append([*map(int, input().split())])

answer = 1000000000
rh, rv, sh, sv = rh - 0.0001, rv - 0.0001, sh - 0.0001, sv - 0.0001
for m in l:
    rhi, rvi, shi, svi, p = m
    h_count = int(max(rh // rhi, sh // shi) + 1)
    v_count = int(max(rv // rvi, sv // svi) + 1)
    answer = min(answer, h_count * v_count * p)
    
    rhi, rvi, shi, svi = rvi, rhi, svi, shi
    h_count = int(max(rh // rhi, sh // shi) + 1)
    v_count = int(max(rv // rvi, sv // svi) + 1)
    answer = min(answer, h_count * v_count * p)
print(answer)