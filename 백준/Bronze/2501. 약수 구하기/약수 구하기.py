p, q = map(int, input().split())

k = 0
for i in range(1, p + 1):
    if p % i == 0:
        k += 1
        if k == q:
            print(i)
            exit()
print(0)