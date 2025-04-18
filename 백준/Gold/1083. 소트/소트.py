import sys

input = sys.stdin.readline

n = int(input())
e = list(map(int, input().split()))
s = int(input())

i = 0
count = 0
e_max_list = sorted(e, reverse = True)
while count != s:
    for j in range(len(e_max_list)):
        max_e = e_max_list[j]
        max_e_i = e.index(max_e)
        if e[i] >= max_e:
            del e_max_list[j]
            i += 1
            break
        if e[i] != max_e and max_e_i <= s - count + i:
            del e_max_list[j]
            del e[max_e_i]
            e.insert(i, max_e)
            count += max_e_i - i
            i += 1
            break
    if i == len(e):
        break

print(' '.join(map(str, e)))