n = int(input())
for i in range(2, int(n ** 0.5) + 1):
    while n % i == 0:
        n = n // i
        print(i)
if n != 1:
    print(n)