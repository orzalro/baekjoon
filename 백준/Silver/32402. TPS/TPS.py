import sys
input = sys.stdin.readline

n = int(input())
chr_coord = [0, 0]
cam_dir = 0
for i in range(n):
    cmd = input().strip()
    if cmd == 'MR': cam_dir = (cam_dir + 1) % 4
    elif cmd == 'ML': cam_dir = (cam_dir - 1) % 4
    else:
        if cmd == 'W': cmd = 0
        elif cmd == 'D': cmd = 1
        elif cmd == 'S': cmd = 2
        elif cmd == 'A': cmd = 3
        dir = (cam_dir + cmd) % 4
        if dir == 0: chr_coord[1] += 1
        elif dir == 1: chr_coord[0] += 1
        elif dir == 2: chr_coord[1] -= 1
        elif dir == 3: chr_coord[0] -= 1
    print(' '.join(map(str, chr_coord)), end = ' ')
    if cam_dir == 0: print(chr_coord[0], chr_coord[1] - 1)
    elif cam_dir == 1: print(chr_coord[0] - 1, chr_coord[1])
    elif cam_dir == 2: print(chr_coord[0], chr_coord[1] + 1)
    elif cam_dir == 3: print(chr_coord[0] + 1, chr_coord[1])