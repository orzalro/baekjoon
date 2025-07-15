import sys
input = sys.stdin.readline

def is_prime(n):
    if n == 1 or n % 2 == 0:
        return 'no'
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return 'no'
    return 'yes'

def calc(n):
    if int(n) == 2:
        return 'yes'
    for i in ['3', '4', '7']:
        if i in n:    
            return 'no'
    if n[0] in ['2', '8', '9']:
        return 'no'
    if n[-1] in ['0', '2', '6', '8']:
        return 'no'
    if is_prime(int(n)) == 'no':
        return 'no'
    else:
        new_n = ''
        for i in n:
            if i in ['0', '1', '2', '5', '8']:
                new_n += i
            elif i == '6':
                new_n += '9'
            elif i == '9':
                new_n += '6'
        return is_prime(int(new_n[::-1]))

n = input().strip()
print(calc(n))