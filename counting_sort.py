def counting_sort(arr, k):
    output = [0] * len(arr)
    count = [0] * k
    for e in arr:
        count[e] += 1
    for i in range(1,k):
        count[i] = count[i] + count[i-1]
    for i in range(len(arr)):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    return output

print(counting_sort([4,2,1,0,5,6,7,11,2,2,7,8,34], 35))
