import sys
input = sys.stdin.readline

v = int(input())
s = input().strip()
count = s.count('A')
if count > v - count: print('A')
elif count < v - count: print('B')
else: print('Tie')