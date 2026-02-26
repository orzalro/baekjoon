stick = input().strip()
stick = stick.replace('()', '!')

answer = 0
stack = 0

for current in stick:
    if current == '(':
        answer += 1
        stack += 1
    elif current == ')':
        stack -= 1
    else:
        answer += stack

print(answer)