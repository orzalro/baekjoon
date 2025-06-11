import sys
input = sys.stdin.readline

c = input().strip()
print('Naver D2' if c in ['N', 'n'] else 'Naver Whale')