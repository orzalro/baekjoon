def solution(m, n, puddles):
    grid = [[1 for _ in range(m)] for _ in range(n)]
    for puddle in puddles:
        pm, pn = puddle
        grid[pn - 1][pm - 1] = 0
        if pm == 1:
            for y in range(pn - 1, n):
                grid[y][pm - 1] = 0
        if pn == 1:
            for x in range(pm - 1, m):
                grid[pn - 1][x] = 0
    
    for y in range(1, n):
        for x in range(1, m):
            if grid[y][x]:
                grid[y][x] = grid[y - 1][x] + grid[y][x - 1]
    print(grid)
    
    answer = grid[n - 1][m - 1]
    return answer % 1000000007