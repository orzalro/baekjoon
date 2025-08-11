import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def calc(n, hp, skill, cd, t, min_t):
    if hp <= 0:
        return t
    elif t >= min_t:
        return min_t
    else:
        use_skill = 1
        for i in range(n):
            temp = cd[:]
            if temp[i] <= t:
                use_skill = 0
                c, d = skill[i]
                temp[i] = t + c
                min_t = min(min_t, calc(n, hp - d, skill, temp, t + 1, min_t))
        if use_skill:
            min_t = min(min_t, calc(n, hp, skill, cd, t + 1, min_t))
        return min_t

n, hp = map(int, input().split())
skill =[[*map(int, input().split())] for _ in range(n)]
cd = [0 for _ in range(n)]
print(calc(n, hp, skill, cd, 0, 101))