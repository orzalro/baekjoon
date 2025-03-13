import sys


m = int(sys.stdin.readline().strip())
s = []

for i in range(m):
    command = sys.stdin.readline().split()
    if command[0] == 'add':
        if command[1] in s:
            continue
        s.append(command[1])
    elif command[0] == 'remove':
        if command[1] in s:
            s.remove(command[1])
    elif command[0] == 'check':
        print(1 if command[1] in s else 0)
    elif command[0] == 'toggle':
        if command[1] in s:
            s.remove(command[1])
        else:
            s.append(command[1])
    elif command[0] == 'all':
        s = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
    elif command[0] == 'empty':
        s = []