import sys


n = int(sys.stdin.readline().strip())
l = []
target = []
for i in range(n):
    l.append(i + 1)
    target.append(int(sys.stdin.readline().strip()))

stack = []
poplist = []
answer = []

for i in target:
    if len(l) > 0 or len(stack):
        if i < l[0] if len(l) > 0 else stack[-1]:
            for j in range(len(stack), 0, -1):
                answer.append('-')
                if i == stack[j - 1]:
                    poplist.append(stack.pop())
                    break
        else:
            for j in range(len(l)):
                j = l.pop(0)
                stack.append(j)
                answer.append('+')
                if i == j:
                    answer.append('-')
                    poplist.append(stack.pop())
                    break

if len(l) == 0 and len(stack) == 0:
    for i in answer:
        print(i)
else:
    print('NO')