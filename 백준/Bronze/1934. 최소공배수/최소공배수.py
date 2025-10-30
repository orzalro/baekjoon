def Euclidean(a, b):
    while b != 0:
        a, b = b, a%b
    return a

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a < b:
        a, b = b, a
    gcd = Euclidean(a, b)
    lcm = a * b // gcd
    print(lcm)