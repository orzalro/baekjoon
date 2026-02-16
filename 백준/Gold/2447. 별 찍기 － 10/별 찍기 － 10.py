def calc(n, c='*'):
    if n == 1:
        return c
    else:
        block = calc(n // 3, c)
        blank = calc(n // 3, ' ')
        
        result = []
        for row in block:
            result.append(row * 3)
        for row in zip(block, blank, block):
            result.append(''.join(row))
        for row in block:
            result.append(row * 3)
        return result

n = int(input())
print(*calc(n), sep='\n')