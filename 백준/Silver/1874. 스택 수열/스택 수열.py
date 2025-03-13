import sys


n = int(sys.stdin.readline().strip())
l = []
target = []
for i in range(n):
    l.append(i + 1)
    target.append(int(sys.stdin.readline().strip()))

def calc(l, target):
    stack = []
    poplist = []
    answer = []

    for i in target:
        if len(l) > 0 or len(stack):
            if i < l[0] if len(l) > 0 else stack[-1]:
                flag = 0
                for j in range(len(stack), 0, -1):
                    answer.append('-')
                    if i == stack[j - 1]:
                        flag = 1
                        poplist.append(stack.pop())
                        break
                if flag == 0:
                    return 'NO'
            else:
                flag = 0
                for j in range(len(l)):
                    j = l.pop(0)
                    stack.append(j)
                    answer.append('+')
                    if i == j:
                        flag = 1
                        answer.append('-')
                        poplist.append(stack.pop())
                        break
                if flag == 0:
                    return 'NO'

    return '\n'.join(answer)
    
print(calc(l, target))