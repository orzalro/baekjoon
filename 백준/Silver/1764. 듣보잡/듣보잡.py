import sys


n, m = map(int, (sys.stdin.readline().split()))

n_list =[]
m_list =[]

for i in range(n):
    n_list.append(sys.stdin.readline().strip())

n_list = set(n_list)

for i in range(m):
    a = sys.stdin.readline().strip()
    if a in n_list:
        m_list.append(a)

print(len(m_list))
m_list.sort()
for i in m_list:
    print(i)