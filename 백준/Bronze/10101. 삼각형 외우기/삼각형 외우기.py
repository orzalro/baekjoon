import sys
input = sys.stdin.readline

a, b, c = [int(input()) for _ in range(3)]
if sum([a, b, c]) != 180:
    print('Error')
else:
    if a == b:
        if a == c:
            print('Equilateral')
        else:
            print('Isosceles')
    elif a == c:
        print('Isosceles')
    elif b == c:
        print('Isosceles')
    else:
        print('Scalene')