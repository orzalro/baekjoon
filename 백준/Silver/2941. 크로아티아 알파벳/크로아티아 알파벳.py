import sys
input = sys.stdin.readline

s = input().strip()
l = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for c in l:
    s = s.replace(c, ' ')
print(len(s))