def calc(n):
    if n % 3 == 0 or '3' in str(n):
        n += 1
        return calc(n)
    return n

def solution(n):
    answer = 0
    for _ in range(n):
        answer += 1
        answer = calc(answer)
        
    return answer