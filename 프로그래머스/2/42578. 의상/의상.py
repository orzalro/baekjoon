def solution(clothes):
    d = {}
    for row in clothes:
        if row[1] in d:
            d[row[1]] += 1
        else:
            d[row[1]] = 1
    
    answer = 1
    for count in d.values():
        answer *= (count + 1)
    
    return answer - 1