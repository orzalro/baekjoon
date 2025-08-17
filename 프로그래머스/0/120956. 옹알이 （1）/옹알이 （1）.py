def solution(babbling):
    answer = 0
    l = ['aya', 'ye', 'woo', 'ma']
    
    for word in babbling:
        for d in l:
            word = word.replace(d, '1')
        try:
            if int(word):
                answer += 1
        except:
            pass
    return answer