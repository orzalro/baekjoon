def solution(wallpaper):
    lux, luy, rdx, rdy = len(wallpaper), len(wallpaper[0]), 0, 0
    for i, row in enumerate(wallpaper):
        for j, col in enumerate(row):
            if col == '#':
                lux, luy, rdx, rdy = min(lux, i), min(luy, j), max(rdx, i + 1), max(rdy, j + 1)
    answer = [lux, luy, rdx, rdy]
    return answer