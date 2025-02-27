import sys

n = int(sys.stdin.readline().strip())

c = 0
m = 0
while True:
    if n <= 6 * m + 1:
        break
    c += 1
    m += c
print(c + 1)