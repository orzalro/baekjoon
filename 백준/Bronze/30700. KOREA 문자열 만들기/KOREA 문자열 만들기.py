import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def calc(c:str, s:str):
    c_d = {'K':'O', 'O':'R', 'R':'E', 'E':'A', 'A':'K'}
    answer = 0
    i = s.find(c)
    if i != -1:
        s = s[i:]
        answer += calc(c_d[c], s) + 1
    return answer

print(calc('K', input().strip()))