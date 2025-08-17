def solution(spell, dic):
    for word in dic:
        flag = 1
        for char in spell:
            if char not in word:
                flag = 0
                break
        if flag:
            return 1

    return 2