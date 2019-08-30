def binary_insert(arr, lo, hi, num):
    if lo == hi:
        if arr[lo] > num:
            return lo
        else:
            return lo + 1
    if lo > hi:
        return lo
    mid = (hi + lo) // 2
    if num < arr[mid]:
        return binary_insert(arr, lo, mid - 1, num)
    elif num > arr[mid]:
        return binary_insert(arr, mid + 1, hi, num)
    else:
        return mid

arr = [1,2,3,4,5,6,7,8,9]
n = len(arr)
num = 10
i = binary_insert(arr, 0, n - 1, num)
arr.append(None)
j = n
while j >= i:
    arr[j] = arr[j-1]
    j -= 1
arr[i] = num

print(arr)
