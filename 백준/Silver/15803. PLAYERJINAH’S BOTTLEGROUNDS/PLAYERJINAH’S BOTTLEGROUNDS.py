import sys
input = sys.stdin.readline

l = []
for i in range(3):
    l.append(list(map(int, input().split())))

if ((l[1][0] - l[0][0]) * (l[2][1] - l[0][1])) - ((l[1][1] - l[0][1]) * (l[2][0] - l[0][0])) == 0:
    print('WHERE IS MY CHICKEN?')
else:
    print('WINNER WINNER CHICKEN DINNER!')