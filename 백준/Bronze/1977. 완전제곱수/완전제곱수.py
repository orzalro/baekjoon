m = int(input())
n = int(input())

total = -1
for i in range(1, 101):
    i = pow(i, 2)
    if m <= i and i <= n:
        if total == -1:
            total, min_num = i, i
        else:
            total += i
    
print(total)
if total != -1:
    print(min_num)
