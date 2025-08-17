import sys
input = sys.stdin.readline

def calc(s):
    if len(dict().fromkeys(s)) == 1:
        return -1
    else:
        for i in range(len(s) // 2):
            if s[i] != s[-(i+1)]:
                return len(s)
        return len(s) - 1
            
s = input().strip()
print(calc(s))