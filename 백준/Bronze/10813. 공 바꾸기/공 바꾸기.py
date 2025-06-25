import sys
input = sys.stdin.readline

n, m = map(int, input().split())
balls = [i + 1 for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    balls[a], balls[b] = balls[b], balls[a]
print(' '.join(map(str, balls)))