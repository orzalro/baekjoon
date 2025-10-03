i = int(input())
[print(' ' * (i - n - 1),'*' * (n * 2 + 1), sep = '') for n in range(i)]
[print(' ' * (i - n - 1),'*' * (n * 2 + 1), sep = '') for n in range(i - 2, -1 , -1)]