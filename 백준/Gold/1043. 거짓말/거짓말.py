import sys

input = sys.stdin.readline

n, m = map(int, input().split())
k_n = list(map(int, input().split()[1:])) # 진실을 아는 사람
p_list = [] # 파티별 오는 사람
for i in range(m):
    p_list.append(list(map(int, input().split()[1:])))

def calc(k_n, p_list):
    if len(k_n) == 0: # 진실을 아는 사람이 없는 경우
        return len(p_list)
    
    visited = k_n
    q = k_n
    while len(q) != 0:
        k = q.pop()
        for i, p in enumerate(p_list):
            if k in p:
                for p_m in p:
                    if p_m not in visited:
                        visited.append(p_m)
                        q.append(p_m)
                del p_list[i]
    return len(p_list)

print(calc(k_n, p_list))