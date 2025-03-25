import sys

input = sys.stdin.readline

n = int(input())

meeting = []
end_time = 0
for i in range(n):
    string = list(map(int, input().split()))
    if string[1] > end_time: end_time = string[1]
    meeting.append(string)
meeting.sort()

count = 0
start = 0

while True:
    end = end_time
    flag = 0
    for i in range(start, len(meeting)):
        if meeting[i][0] == meeting[i][1] and i == start:
            start = i + 1
            flag = 1
            break
        if meeting[i][0] >= end:
            start = i
            flag = 1
            break
        if meeting[i][1] < end:
            end = meeting[i][1]
        flag = 2
    if flag == 0:
        break
    elif flag == 1:
        count += 1
    elif flag == 2:
        count += 1
        break
    
print(count)