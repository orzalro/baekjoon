import sys

count = int(sys.stdin.readline().strip())
number = sys.stdin.readline().strip()
answer = 0
for i in range(count):
    answer += int(number[i])
print(answer)