def solution(land):
    dp = [land[i][:] for i in range(len(land))]
    for i in range(1, len(land)):
        for j in range(4):
            dp[i][j] += max([dp[i - 1][k] for k in range(4) if k != j]) 
    return max(dp[-1])