def cal(arr):
    swaps = False
    for i in range(len(arr)-1):
        for j in range(len(arr)):
            if arr[i] != -1 and (arr[i] - arr[j]) == 1:
                arr[i] = -1
                swaps = True
    if swaps == True:
        return cal(arr)
    else:
        count = 0
        for i in arr:
            if i != -1:
                count++
        return count
                
