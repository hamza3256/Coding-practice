def solution(arr):
    left = sumUp(arr,2)
    right = sumUp(arr, 3)
    if (left == right):
        return "" 
    if (left > right):
        return "Left"
    else:
        return "Right"
    
    
def sumUp(arr, i):
    if i - 1 < len(arr):
        if arr[i-1] == -1:
            return 0
        return arr[i-1] + sumUp(arr, i*2) + sumUp(arr, i*2 + 1)
    return 0
    
a = [3,6,2,9,5,10,5,1,2,3,4,1]
print(solution(a))