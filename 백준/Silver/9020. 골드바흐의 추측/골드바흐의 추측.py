import sys
input = sys.stdin.readline

def eratosthenes(num):
    MAX = num + 1
    LIM = int(num ** 0.5) + 1
    RSET = lambda strt, end, gap: set(range(strt, end, gap))
    
    # 5 (mod 6)과 1 (mod 6)을 참으로 설정한다. 이들은 2의 배수도 아니고 3의 배수도 아닌 숫자집합이다.
    # 단, 1은 소수가 아니기에 1 (mod 6)은 7부터 시작한다.
    prime = RSET(5, MAX, 6) | RSET(7, MAX, 6)
    if num > 2: prime.add(3) # 3 추가
    if num > 1: prime.add(2) # 2 추가
    for i in range(5, LIM, 6):
        # 5 (mod 6) 부분
        if i in prime:
            prime -= RSET(i * i, MAX, i * 6) | RSET(i * (i + 2), MAX, i * 6)
        # 1 (mod 6) 부분
        j = i + 2
        if j in prime:
            prime -= RSET(j * j, MAX, j * 6) | RSET(j * (j + 4), MAX, j * 6)

    return sorted(prime)

# 10000까지의 소수 구하기
prime_set = eratosthenes(10000)

t = int(input())
for _ in range(t):
    n = int(input())

    # n을 반으로 나눠서 소수집합에 있는지 확인 (없으면 1씩 더해서 나올때까지 확인). 처음 나온 소수가 소수집합에서 몇번째 수인지 확인
    temp = n // 2
    while True:
        if temp in prime_set:
            i = prime_set.index(temp)
            break
        temp += 1

    # 해당 소수와 n의 차가 소수집합에 있는지 확인. 없으면 다음으로 큰 소수 탐색
    while True:
        diff = n - prime_set[i]
        if diff in prime_set:
            print(diff, prime_set[i])
            break
        i += 1