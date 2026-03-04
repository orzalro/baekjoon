n = int(input())

def calc(row, unused_cols, diag, diag_r):
    if row == n:
        return 1

    count = 0
    for col in list(unused_cols):
        if (row - col) not in diag and (row + col) not in diag_r:
            unused_cols.remove(col)
            diag.add(row - col)
            diag_r.add(row + col)

            count += calc(row + 1, unused_cols, diag, diag_r)

            unused_cols.add(col)
            diag.remove(row - col)
            diag_r.remove(row + col)
    return count

print(calc(0, set(range(n)), set(), set()))