def solution(numbers):
    max_n = max(numbers)
    numbers.remove(max_n)
    answer = max_n * max(numbers)
    return answer