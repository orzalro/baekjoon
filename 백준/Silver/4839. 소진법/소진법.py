import sys
input = sys.stdin.readline

def calc(n):
    prime = [223092870, 9699690, 510510, 30030, 2310, 210, 30, 6, 2]
    prime_dict = {223092870:'2*3*5*7*11*13*17*19*23', 9699690:'2*3*5*7*11*13*17*19', 510510:'2*3*5*7*11*13*17', 30030:'2*3*5*7*11*13', 2310:'2*3*5*7*11', 210:'2*3*5*7', 30:'2*3*5', 6:'2*3', 2:'2'}
    answer = []
    for i in prime:
        temp = n // i
        n = n % i
        if temp != 0:
            answer.append(f'{temp}*{prime_dict[i]}')
        if n == 0:
            break
    if n:
        answer.append('1')
    return answer

while True:
    n = int(input())
    if n == 0:
        break
    print(n, '=', end=' ')
    print(*calc(n)[::-1], sep=' + ')