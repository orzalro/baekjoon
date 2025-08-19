def solution(sizes):
    max_w, max_h = (0, 0)
    for w, h in sizes:
        max_w = max(max_w, h, w)
        max_h = max(max_h, min(h, w))
    
    return max_w * max_h