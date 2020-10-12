####INCOMPLETE#### 4/15 tests passed

def minimumSwaps(arr):
    n = 0
    while(sorted(arr) != arr):
        for i in range(len(arr)-1):
            print(arr[i], arr[i+1])
            if len(arr)-2> i:
                for j in range(i+1, len(arr)-1):
                    if arr[j] < arr[j+1] and arr[i] > arr[j]:
                        arr[i], arr[j] = arr[j], arr[i]
                        n+=1
                        break
            elif arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                n+=1
                break
    return n
