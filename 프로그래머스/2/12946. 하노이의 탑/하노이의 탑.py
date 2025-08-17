def hanoi(answer, start, end, temp, n):
    if n == 1:
        answer.append([start, end])
    else:
        hanoi(answer, start, temp, end, n - 1)
        answer.append([start, end])
        hanoi(answer, temp, end, start, n - 1)
        

def solution(n):
    answer = []
    hanoi(answer, 1, 3, 2, n)
    return answer