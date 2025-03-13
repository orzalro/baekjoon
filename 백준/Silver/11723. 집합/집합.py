import sys


m = int(sys.stdin.readline().strip())
s = []

for i in range(m):
    command = sys.stdin.readline().split()
    if len(command) > 1:
        c = int(command[1])
    if command[0] == 'add':
        if c in s:
            continue
        s.append(c)
    elif command[0] == 'remove':
        if c in s:
            s.remove(c)
    elif command[0] == 'check':
        print(1 if c in s else 0)
    elif command[0] == 'toggle':
        if c in s:
            s.remove(c)
        else:
            s.append(c)
    elif command[0] == 'all':
        s = list(range(1, 21))
    elif command[0] == 'empty':
        s.clear()