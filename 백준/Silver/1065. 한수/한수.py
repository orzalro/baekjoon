import sys
input = sys.stdin.readline

def calc(n):
    n = str(n)
    pre = None
    temp = None
    for c in n:
        if pre != None:
            if temp != None:
                if temp == pre - int(c):
                    pre = int(c)
                else:
                    return False
            else:
                temp = pre - int(c)
                pre = int(c)
        else:
            pre = int(c)
    return True

n = int(input())
count = 0
for i in range(1, n + 1):
    if calc(i):
        count += 1
print(count)