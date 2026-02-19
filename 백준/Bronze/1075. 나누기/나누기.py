n = int(input())
f = int(input())
n = n - n % 100

lownum = sorted([i for i in range(n, n + 100) if i % f == 0])[0]

print(f'{str(lownum)[-2:]}')