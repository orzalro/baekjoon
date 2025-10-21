import sys
input = sys.stdin.readline

x_1, y_1 = map(int, input().split())
x_2, y_2 = map(int, input().split())
x_3, y_3 = map(int, input().split())

if x_1 == x_2: print(x_3, end=' ')
elif x_1 == x_3: print(x_2, end=' ')
else: print(x_1, end=' ')
if y_1 == y_2: print(y_3)
elif y_1 == y_3: print(y_2)
else: print(y_1)