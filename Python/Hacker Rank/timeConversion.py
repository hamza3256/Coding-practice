def timeConversion(s):
    if s[-2:] == 'PM' and int(s[:2]) < 12:
        a = int(s[:2]) + 12
        if a > 23:
            a -= 24
        s = "{0:0=2d}".format(a) + s[2:-2]
    else:
        if s[:2] == '12' and s[-2:] == 'AM':
            s = "00" + s[2:-2]
        else:
            s = s[:-2]
    return s


s = "12:45:54PM"
print(timeConversion(s))
