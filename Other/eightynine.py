def st(n):
    c = 0; m = 85
    while m < n:
        if n == 1:
            continue
        s = str(m)
        m = 0
        for i in s:
            m += int(i)**2
        if m == 89:
            c+=1
        if m> 100000:
            print(c)
    return c
print(st(1000000))
