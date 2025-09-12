import sys
input = sys.stdin.readline

s = input().strip().upper()
d = {c:s.count(c)for c in dict.fromkeys(s)}
sorted_d = sorted(d, key= lambda x:d[x], reverse=True)
if len(sorted_d) > 1:
    if d[sorted_d[0]] == d[sorted_d[1]]:
        print('?')
    else:
        print(sorted_d[0])
else:
    print(sorted_d[0])