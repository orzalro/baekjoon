import sys
input = sys.stdin.readline

def E(x, a, b):
    x -= 65
    return (a * x + b) % 26 + 65

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    s = input().strip()
    print(''.join(chr(E(ord(i), a, b)) for i in s))