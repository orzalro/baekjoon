import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    students = [*map(int, input().split())]
    mean = sum(students[1:]) / students[0]
    print(f'{sum([1 for i in students[1:] if i > mean]) / students[0] * 100:.3f}%')