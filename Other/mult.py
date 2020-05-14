# find and then sum all multiples of 3 and 5, below 1000

def find(s, n, y):
    arr=[]
    for c in range(1,y):
        if (c % s == 0 and c not in arr) or (c % n == 0 and c not in arr):
            arr.append(c)
    a = sum(arr)
    return a

print(find(3,5, 1000))
