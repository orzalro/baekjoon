import sys

n = int(sys.stdin.readline().strip())


for i in range(n):
    cos_dict = {}
    cos_num = int(sys.stdin.readline().strip())
    for j in range(cos_num):
        costype = sys.stdin.readline().split()[1]
        if costype in cos_dict:
            cos_dict[costype] += 1
        else:
            cos_dict[costype] = 1
    answer = 1
    for i in cos_dict.values():
        answer *= i + 1
    print(answer - 1)