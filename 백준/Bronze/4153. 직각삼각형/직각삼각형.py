import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a + b + c == 0: break
    if max([a, b, c]) ** 2 * 2 == a ** 2 + b ** 2 + c ** 2: print('right')
    else: print('wrong')