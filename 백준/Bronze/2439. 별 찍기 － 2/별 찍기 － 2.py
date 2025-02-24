import sys

number = int(sys.stdin.readline().strip())

for i in range(1, number + 1):
    line = f'{' ' * (number - i)}{'*' * i}'
    print(line)