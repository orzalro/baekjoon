import sys


n, m = map(int, (sys.stdin.readline().split()))
site_dict = {}

for i in range(n):
    string = sys.stdin.readline().split()
    site_dict[string[0]] = string[1]

for i in range(m):
    string = sys.stdin.readline().strip()
    print(site_dict[string])