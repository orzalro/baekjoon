import sys
input = sys.stdin.readline

def calc(num):
    num_str = str(num)
    if len(num_str) % 2 == 1:
        return num
    else:
        result = ''
        pre_num = -1
        for i in range(0, len(num_str), 2):
            if pre_num != num_str[i + 1]:
                result += num_str[i + 1] * int(num_str[i])
                pre_num = num_str[i + 1]
            else:
                return num
        if result == num_str:
            return num
        else:
            return calc(int(result))

i = 1
while True:
    n = int(input())
    if n == 0:
        break
    print(f'Test {i}:', calc(n))
    i += 1