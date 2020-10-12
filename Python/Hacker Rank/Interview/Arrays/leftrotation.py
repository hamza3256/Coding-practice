def rotLeft(a, d):
    for _ in range(d):
        a.append(a.pop(0))
    return a
