import sys

n = int(sys.stdin.readline().strip())

def round(n):
    if n - int(n) >= 0.5:
        return int(n) + 1
    else:
        return int(n)

def calc(n):
    if n == 0:
        return 0
    d = []
    for i in range(n):
        d.append(int(sys.stdin.readline().strip()))

    d.sort()
    r = round(n * 0.15)
    if r != 0 : d = d[r:-r]
    total = sum(d)
    if total == 0:
        return 0
    
    return round(total/len(d))

print(calc(n))