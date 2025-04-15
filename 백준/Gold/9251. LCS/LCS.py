import sys

input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

lcs = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if i == 0 or j == 0: lcs[i][j] = 0
        elif str1[i - 1] == str2[j - 1]: lcs[i][j] = lcs[i - 1][j - 1] + 1
        else: lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])

print(max(lcs[-1]))