import timeit, functools

def diagonalDifference(arr):
    left = right = 0
    lenA = len(arr)
    for i in range(lenA):
        left += arr[i][i]
        right += arr[i][lenA-1-i]
    return abs(left-right)

def diagonalDifference1(arr):
    left = right = 0
    for i in range(len(a)):
        left += arr[i][i]
        right += arr[i][len(a)-1-i]
    return abs(left-right)

a = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
t = timeit.timeit(functools.partial(diagonalDifference,a), number = 100000)
t2 = timeit.timeit(functools.partial(diagonalDifference1,a), number = 100000)
t3= timeit.timeit(functools.partial(diagonalDifference,a), number = 100000)
t4 = timeit.timeit(functools.partial(diagonalDifference1,a), number = 100000)
t5 = timeit.timeit(functools.partial(diagonalDifference,a), number = 100000)
t6 = timeit.timeit(functools.partial(diagonalDifference1,a), number = 100000)
t7 = timeit.timeit(functools.partial(diagonalDifference,a), number = 100000)
t8 = timeit.timeit(functools.partial(diagonalDifference1,a), number = 100000)
t9 = timeit.timeit(functools.partial(diagonalDifference,a), number = 100000)
t10 = timeit.timeit(functools.partial(diagonalDifference1,a), number = 100000)
t11 = timeit.timeit(functools.partial(diagonalDifference,a), number = 100000)
t12 = timeit.timeit(functools.partial(diagonalDifference1,a), number = 100000)
print(f'Time taken with lenA: {(t+t3+t5+t7+t9+t11)/6} \nTime taken without lenA: {((t2+t4+t6+t8+t10+t12)/6)}')
