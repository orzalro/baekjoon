import sys


m = int(sys.stdin.readline().strip())
s = dict()
for i in range(1, 21):
    s[i] = 0

for i in range(m):
    command = sys.stdin.readline().split()
    if len(command) > 1:
        c = int(command[1])
    if command[0] == 'add':
        s[c] = 1
    elif command[0] == 'remove':
        s[c] = 0
    elif command[0] == 'check':
        print(s[c])
    elif command[0] == 'toggle':
        s[c] = 0 if s[c] == 1 else 1
    elif command[0] == 'all':
        for i in range(1, 21):
            s[i] = 1
    elif command[0] == 'empty':
        for i in range(1, 21):
            s[i] = 0