import sys

input = sys.stdin.readline

a, b = map(int, (input().split()))

def bfs(a, b):
    q = [a]
    new_q = []
    visited = set()
    count = 1

    while len(q) != 0:
        for num in q:
            if num == b:
                return count
            else:
                if (num * 10 + 1) not in visited and (num * 10 + 1) <= b: visited.add(num * 10 + 1); new_q.append(num * 10 + 1)
                if (num * 2) not in visited and (num * 2) <= b: visited.add(num * 2); new_q.append(num * 2)
        q = new_q
        new_q = []
        count += 1

    return -1

print(bfs(a, b))