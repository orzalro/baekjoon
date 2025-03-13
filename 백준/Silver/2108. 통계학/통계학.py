import sys


n = int(sys.stdin.readline().strip())

l = []
for i in range(n):
    l.append(int(sys.stdin.readline().strip()))

print(round(sum(l)/ len(l) + 0.01)) # 산술평균 첫째 자리 반올림
l.sort()
print(l[len(l) // 2]) # 중앙값
r = max(l) - min(l) # 범위

d = dict()
for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
dmax = max(d.values())
maxnum = []
for i in d:
    if d[i] == dmax:
        maxnum.append(i)
print(maxnum[0] if len(maxnum) < 2 else maxnum[1]) # 최빈값

print(r)