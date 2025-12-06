n, b = input().split()
b = int(b)

answer = 0
for i, number in enumerate(n[::-1]):
    if number.isnumeric():
        answer += int(number) * b ** i
    else:
        answer += (ord(number) - 55) * b ** i
print(answer)