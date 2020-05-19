def addingCommasToNumber(n):
    s = str(n); c= 0
    for i in range(len(s)-1,-1,-1):
        if (len(s) - i - c) % 3 == 0 and i != 0:
            s = s[:i] + "," + s[i:]
            c+=1
    return s
