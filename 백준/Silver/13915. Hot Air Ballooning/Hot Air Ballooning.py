import sys
input = sys.stdin.readline


while True:
    try:
        n = int(input())
        s = set()
        for _ in range(n):
            b = input().strip()
            s.add(''.join(sorted(dict.fromkeys(b))))
        print(len(s))
    except:
        break