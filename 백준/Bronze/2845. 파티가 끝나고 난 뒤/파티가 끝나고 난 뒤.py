l, p = map(int, input().split())
n = l * p 
print(*[int(i) - n for i in input().split()])