import sys
input = sys.stdin.readline

def calc(x, r, c):
    if x == 1:
        return 'GABRIEL'
    elif x == 2:
        if r * c % 2: return 'RICHARD'
        else: return 'GABRIEL'
    elif x == 3:
        if r * c % 3 or r * c < 4: return 'RICHARD'
        else: return 'GABRIEL'     
    else:
        if r * c >= 12: return 'GABRIEL'
        else: return 'RICHARD'

t = int(input())
for i in range(t):
    x, r, c = map(int, input().split())
    print(f'Case #{i + 1}: {calc(x, r, c)}')