import sys
input = sys.stdin.readline

word = input().strip()
sec = 0
for char in word:
    if char in 'ABC':
        sec += 3
    elif char in 'DEF':
        sec += 4
    elif char in 'GHI':
        sec += 5
    elif char in 'JKL':
        sec += 6
    elif char in 'MNO':
        sec += 7
    elif char in 'PQRS':
        sec += 8
    elif char in 'TUV':
        sec += 9
    elif char in 'WXYZ':
        sec += 10
    
print(sec)