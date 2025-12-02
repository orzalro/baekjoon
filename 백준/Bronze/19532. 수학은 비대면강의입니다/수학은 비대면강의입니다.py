a, b, c, d, e, f = map(int, input().split())

if (b * d - a * e) != 0:
    y = (c * d - a * f) // (b * d - a * e)
else:
    y = 0
if a != 0:
    x = (c - b * y) // a
elif d != 0:
    x = (f - e * y) // d
else:
    x = 0
print(x, y)

# ax + by = c
# dx + ey = f

# adx + bdy = cd
# adx + aey = af

# bdy - aey = cd - af

# (bd - ae)y = cd - af
# y = (cd - af) / (bd - ae)

# x = (c - by) / a