import sys
input = sys.stdin.readline

n = int(input())
deq = []
for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'push_front':
        deq.insert(0, cmd[1])
    if cmd[0] == 'push_back':
        deq.append(cmd[1])
    if cmd[0] == 'pop_front':
        try: print(deq.pop(0))
        except: print(-1)
    if cmd[0] == 'pop_back':
        try: print(deq.pop())
        except: print(-1)
    if cmd[0] == 'size':
        print(len(deq))
    if cmd[0] == 'empty':
        print(int(not len(deq)))
    if cmd[0] == 'front':
        try: print(deq[0])
        except: print(-1)
    if cmd[0] == 'back':
        try: print(deq[-1])
        except: print(-1)