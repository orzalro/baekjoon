import sys
from itertools import permutations
input = sys.stdin.readline

def ismagic(l, a):
    for i in range(l - 1):
        for j in range(i + 1, l):
            if a[i][j] != a[j][i]:
                return False
    return True

l, n = map(int, input().split())
words = [input().strip() for _ in range(n)]
words.sort()
answer = 'NONE'

for p in permutations(range(n), l):
    temp = []
    for i in p:
        temp.append(words[i])
    if ismagic(l, temp):
        answer = temp
        break

if answer == 'NONE':
    print(answer)
else:
    print(*answer, sep='\n')