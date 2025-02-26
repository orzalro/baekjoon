import sys

t = int(sys.stdin.readline().strip())

for i in range(t):
    a = sys.stdin.readline().strip()
    count = 1
    score = 0
    for j in a:
        if j == 'O':
            score += count
            count += 1
        else:
            count = 1
    print(score)