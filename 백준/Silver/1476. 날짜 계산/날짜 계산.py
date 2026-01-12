e, s, m = map(int, input().split())
n = 0
while True:
    if n % 15 + 1 == e and n % 28 + 1 == s and n % 19 + 1 == m:
        print(n + 1)
        break
    else:
        n += 1