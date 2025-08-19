def solution(participant, completion):
    d = {}
    for name in participant:
        if name in d:
            d[name] += 1
        else:
            d[name] = 1
    for name in completion:
        if name in d:
            d[name] -= 1
        else:
            return name
    
    for key, values in d.items():
        if values != 0: return key