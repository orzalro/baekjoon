import sys
input = sys.stdin.readline

n = int(input())

def calc(floor, start, end):
    if floor == 1:
        result.append(f'{start} {end}')
    else:
        temp = 6 - start - end
        calc(floor - 1, start, temp)
        result.append(f'{start} {end}')
        calc(floor - 1, temp, end)

result = []
calc(n, 1, 3)
print(len(result), *result, sep='\n')