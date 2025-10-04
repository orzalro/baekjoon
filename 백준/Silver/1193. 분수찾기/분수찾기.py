x = int(input())
i = 1
while True:
    x -= i
    i += 1
    if x == 0:
        print(f'1/{i - 1}' if i % 2 == 0 else f'{i - 1}/1')
        exit()
    elif x < i:
        print(f'{x}/{i - x + 1}' if i % 2 == 0 else f'{i - x + 1}/{x}')
        exit()