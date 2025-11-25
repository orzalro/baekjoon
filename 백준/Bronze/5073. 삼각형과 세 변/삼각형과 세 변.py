import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())
    if a + b + c == 0: break
    if sum(sorted([a, b, c])[:2]) <= max([a, b, c]):
        print('Invalid')
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