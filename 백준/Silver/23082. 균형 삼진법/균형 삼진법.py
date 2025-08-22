import sys
input = sys.stdin.readline

def calc(n):
    if n == 0:
        return 0
    
    minus = 0
    if n < 0:
        minus = 1
        n = -n
    
    answer = []
    while n > 0:
        r = n % 3
        if r == 2:
            r = -1
            answer.append("T")
        else:
            answer.append(str(r))
        n -= r
        n = n // 3
    
    result = ''.join(reversed(answer))
    if minus:
        result = result.translate(str.maketrans('T01','10T'))
    return result

n = int(input())
print(calc(n))