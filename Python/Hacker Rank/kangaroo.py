def kangaroo(x1, v1, x2, v2):
    if x1 >= x2 and v1 > v2 or x1 <= x2 and v1 < v2 or v1 == v2:
        return 'NO'
    d1 = x1; d2 = x2
    while 1:
        if d1 == d2:
            return 'YES'
        elif abs(d1 - d2) > abs(x1 - x2):
            return 'NO'
        d1 += v1
        d2 += v2
    return 'NO'