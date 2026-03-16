import sys
from itertools import combinations
input = sys.stdin.readline

l, c = map(int, input().split())
chars = sorted(input().split())

print(*[''.join(password) for password in combinations(chars, l)
        if any(char in "aeiou" for char in password) and
        len([char for char in password if char not in "aeiou" ]) > 1],
        sep='\n')