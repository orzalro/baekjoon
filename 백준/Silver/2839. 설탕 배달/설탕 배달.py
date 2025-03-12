import sys

n = int(sys.stdin.readline().strip())

def calc(n):
    minimum = n
    if n in [1, 2, 4, 7]:
        return -1
    if n % 5 == 0:
        minimum = n // 5
    if n % 3 == 0:
        if minimum > n // 3:
            minimum = n // 3
    count = 0
    while True:
        n5 = n // 5 - count
        n3 = (n % 5 + count * 5) // 3 
        n1 = n - (n5 * 5 + n3 * 3)
        count += 1
        if n1 == 0:
            if minimum >= n5 + n3:
                minimum = n5 + n3
            break
    return minimum
            
print(calc(n))