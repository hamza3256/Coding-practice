def countApplesAndOranges(s, t, a, b, apples, oranges):
    l = max(len(apples), len(oranges))
    for i in range(l):
        if i <= len(apples) - 1:
            apples[i] += a
        if i <= len(oranges) - 1:
            oranges[i] += b
    a1 = b1 = 0
    for i in range(l):
        if i <= len(apples) - 1:
            if apples[i] >= s and apples[i] <= t:
                a1 += 1
        if i <= len(oranges) - 1:
            if oranges[i] >= s and oranges[i] <= t:
                b1 += 1
    print(a1)
    print(b1)
