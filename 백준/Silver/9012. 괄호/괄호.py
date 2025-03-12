import sys

n = int(sys.stdin.readline().strip())

for i in range(n):
    string = sys.stdin.readline()[:-1]
    if string == '.':
        break
    str_stack = []
    for i in range(len(string)):
        if string[i] in '()[]':
            str_stack.append(string[i])

    pop_stack = []
    for i in range(len(str_stack)):
        pop_stack.append(str_stack.pop(0))
        if len(pop_stack) >= 2:
            if pop_stack[-2] == '(' and pop_stack [-1] == ')':
                del pop_stack[-2:]
    print('NO' if pop_stack else 'YES')