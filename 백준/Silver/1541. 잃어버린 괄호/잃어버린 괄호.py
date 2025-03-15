import sys

input = sys.stdin.readline

string = input().strip().split('-')

if len(string) > 1:
    total = 0
    for i in string[1:]:
        total += sum(map(int, i.split('+')))
    print(sum(map(int, string[0].split('+'))) - total)
else:
    print(sum(map(int, string[0].split('+'))))