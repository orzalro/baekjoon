import sys
input = sys.stdin.readline

n, k = map(int, input().split())
# q에 출력 저장, i에 다음에 탐색할 사람을 저장
l = [str(num) for num in range(1, n + 1)]
q = []
i = 0

# l에서 i번째 사람을 제거한뒤 q에 저장
while 0 < n:
    i = (i + k - 1) % n
    q.append(l.pop(i))
    n -= 1
print('<' + ', '.join(q) + '>')