import sys
input = sys.stdin.readline

def eratosthenes(num):
    prime = set(range(5, num + 1, 6)) | set(range(7, num + 1, 6))
    if num > 1: prime.add(2)
    if num > 2: prime.add(3)

    for i in range(5, int(num ** 0.5) + 1, 6):
        j = i + 2
        if i in prime:
            prime -= set(range(i * i, num + 1, i * 6)) | set(range(i * (i + 2), num + 1, i * 6))
        if j in prime:
            prime -= set(range(j * j, num + 1, j * 6)) | set(range(j * (j + 4), num + 1, j * 6))

    return prime

numbers = []
while True:
    n = int(input())
    if n == 0: break
    numbers.append(n)

prime = eratosthenes(max(numbers) * 2)
for n in numbers:
    print(len([num for num in prime if num > n and num <= n * 2]))