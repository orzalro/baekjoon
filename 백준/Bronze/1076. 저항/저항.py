import sys
input = sys.stdin.readline

d = {'black': 0,'brown': 1,'red': 2,'orange': 3,'yellow': 4,'green': 5,'blue': 6,'violet': 7,'grey': 8,'white': 9}
l = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]

answer = 0

for i in range(3):
    if i == 0:
        answer += d[input().strip()] * 10
    elif i == 1:
        answer += d[input().strip()]
    else:
        answer *= l[d[input().strip()]]

print(answer)