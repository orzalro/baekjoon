answer = 0
temp = 1
for _ in range(int(input())):
    answer, temp = temp, answer + temp
print(answer)