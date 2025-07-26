import sys
input = sys.stdin.readline

n = int(input())
s_l = []
for i in range(n):
    s_l.append(input().strip())

s_l.sort()
def calc(s:str):
    i = len(s) * 1000 + sum([int(num) for num in s if num.isdigit()])
    return i
print(*sorted(s_l, key=calc), sep='\n')