n = int(input())
total = sum([int(input()) for _ in range(n)])
if total > n // 2:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')