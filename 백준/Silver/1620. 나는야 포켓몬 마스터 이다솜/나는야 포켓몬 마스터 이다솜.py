import sys


n, m = map(int, (sys.stdin.readline().split()))
monster_keyname = {}

for i in range(1, n + 1):
    monster_keyname[sys.stdin.readline().strip()] = i

monster_keynumber = {v:k for k, v in monster_keyname.items()}

for i in range(m):
    q = sys.stdin.readline().strip()
    if 48 <= ord(q[0]) <= 57:
        print(monster_keynumber[int(q)])
    else:
        print(monster_keyname[q])