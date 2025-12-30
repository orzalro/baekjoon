n = input().strip()
d = {key:n.count(str(key)) for key in range(10)}
l = list(d.values())
l[6] = (l[6] + l.pop() + 1) // 2
print(max(l))