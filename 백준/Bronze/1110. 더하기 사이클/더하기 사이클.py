import sys
input = sys.stdin.readline

n = int(input())
temp = n
count = 0
while True:
    temp = int(str(temp)[-1] + str(sum([temp // 10, temp % 10]))[-1])
    count +=1
    if temp == n:
        break
print(count)