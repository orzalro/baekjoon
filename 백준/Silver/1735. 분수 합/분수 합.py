a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

def calc(a, b):
    while True:
        a, b = b, a % b
        if b == 0:
            return a

lcm = b1 * b2 // calc(b1, b2)
a3, b3 = lcm // b1 * a1 + lcm // b2 * a2, lcm

gcd = calc(a3, b3)
print(a3 // gcd, b3 // gcd)