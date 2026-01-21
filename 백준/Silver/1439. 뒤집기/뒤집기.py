import sys
input = sys.stdin.readline

from itertools import groupby

s = input().strip()
result = ''.join(k for k, _ in groupby(s))
print(min(result.count('0'), result.count('1')))