import sys
input = sys.stdin.readline

t = int(input())
v_dict = {'kg':2.2046, 'lb':0.4536, 'l':0.2642, 'g':3.7854}
u_dict = {'kg':'lb', 'lb':'kg', 'l':'g', 'g':'l'}

for i in range(t):
    v, u = map(str, input().split())
    print(f'{float(v) * v_dict[u]:0.4f} {u_dict[u]}')