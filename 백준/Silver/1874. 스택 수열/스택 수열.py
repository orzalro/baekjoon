import sys


n = int(sys.stdin.readline().strip())
l = dict()
target = []
for i in range(n):
    l[i + 1] = 1
    target.append(int(sys.stdin.readline().strip()))

def calc(l, target):
    answer = ''
    pre = 0
    for i in target:
        if i > pre:
            answer += ('+ ' * (sum(l[j] for j in range(pre + 1, i + 1))) + '- ')
            pre = i
            l[i] = 0
        else:
            if sum(l[j] for j in range(i + 1, pre)) == 0:
                answer += ('- ')
                pre = i
                l[i] = 0
            else:
                return 'NO'

    return '\n'.join(answer.split())
    
print(calc(l, target))

# 높거나 바로 다음 수인 경우만 허용