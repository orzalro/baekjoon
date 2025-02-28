import sys

while True:
    a = sys.stdin.readline().strip()
    if int(a) == 0: break
    answer = 'yes'
    for i in range(len(a) // 2):
        if a[i] != a[- 1 - i]:
            answer = 'no'
            break
    print(answer)