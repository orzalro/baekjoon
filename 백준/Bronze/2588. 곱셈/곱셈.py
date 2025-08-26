a = int(input())
b = input().strip()

for n in b[::-1]:
    print(a * int(n))
print(a * int(b))