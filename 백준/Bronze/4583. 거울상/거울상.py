import sys
input = sys.stdin.readline

mirror = {'b':'d', 'd':'b', 'p':'q', 'q':'p', 'i':'i', 'o':'o', 'v':'v', 'w':'w', 'x':'x'}

while True:
    s = input().strip()
    if s == '#': break
    else:
        answer = ''
        for i in range(1, len(s) + 1):
            if s[-i] in mirror: answer = ''.join([answer, mirror[s[-i]]])
            else: answer = 'INVALID'; break
    print(answer)