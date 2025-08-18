def solution(s):
    s = [row for row in s.split('}') if len(row)]
    s = [row.replace('{', '') for row in s]
    s = [[int(num) for num in row.split(',') if len(num)] for row in s]
    answer = []
    for i in range(1, len(s) + 1):
        for d in s:
            if len(d) == i:
                d = set(d) - set(answer)
                for n in d:
                    answer.append(n)
                break
    return answer