n, b = map(int, input().split())
l = []
while n >= b:
    l.append(n % b)
    n = n // b
l += [n]

def to_char(n):
    if n < 10:
        return n
    else:
        return chr(n + 55)

print(*map(to_char, l[::-1]), sep='')