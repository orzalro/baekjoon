def draw(n):
    if n == 0:
        return '*'
    else:
        return '*' + ' ' * (2 * n - 1) + '*'

n = int(input())
for i in range(n):
    if i == n - 1:
        print('*' * (2 * i + 1))
    else:
        print(' ' * (n - i - 1), draw(i), sep='')