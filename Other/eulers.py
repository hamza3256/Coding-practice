def _factorial(n):
    factorial = 1
    if n >= 1:
        for i in range(1,int(n)+1):
            factorial *= i
    return factorial

def e(n):
    x = 0
    for i in range(0,n+1):
        x+= 1/_factorial(i)
    return x

print(e(10))
