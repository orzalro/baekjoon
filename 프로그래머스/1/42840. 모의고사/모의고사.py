def solution(answers):
    count = [0, 0, 0]
    answer1 = [1, 2, 3, 4, 5]
    answer2 = [2, 1, 2, 3, 2, 4, 2, 5]
    answer3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i, n in enumerate(answers):
        if n == answer1[i % 5]:
            count[0] += 1
        if n == answer2[i % 8]:
            count[1] += 1
        if n == answer3[i % 10]:
            count[2] += 1
    max_count = max(count)
    answer = [i + 1 for i, c in enumerate(count) if c == max_count]
    return answer