n = int(input())

dp0 = [0]
dp1 = [1]

for _ in range(n - 1):
    temp0 = dp0[-1] + dp1[-1]
    temp1 = dp0[-1]
    dp0.append(temp0)
    dp1.append(temp1)

print(dp0[-1] + dp1[-1])