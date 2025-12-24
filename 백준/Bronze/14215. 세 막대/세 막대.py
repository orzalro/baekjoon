l = sorted(map(int, input().split()))
if l[1] == l[2]:
    print(l[1] * 2 + l[0])
else:
    print(l[0] + l[1] + min(l[2], l[0] + l[1] - 1))