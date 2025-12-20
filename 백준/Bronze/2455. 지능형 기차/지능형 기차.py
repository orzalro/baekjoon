answer = 0
temp = 0
for _ in range(4):
    a, b = map(int, input().split())
    temp = temp - a + b
    answer = max(answer, temp)
print(answer)