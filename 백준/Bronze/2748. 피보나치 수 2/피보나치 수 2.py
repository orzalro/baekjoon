pre = 0
cur = 1
for _ in range(int(input())):
    pre, cur = cur, pre + cur
print(pre)