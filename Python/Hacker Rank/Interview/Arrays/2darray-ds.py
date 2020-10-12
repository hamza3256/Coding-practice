def hourglassSum(arr):
    sumArr = []
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            sumArr.append(helper(arr, i, j))
    return max(sumArr)

def helper(arr, x, y):
    s = 0
    for i in range(x, x+3):
        for j in range(y, y+3):
            if (i-x == 1) & (j-y == 0 or j-y == 2):
                continue
            s += arr[i][j]
    return s
