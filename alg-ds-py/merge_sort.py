def merge(ar1, ar2):
    i = 0
    j = 0
    n1 = len(ar1)
    n2 = len(ar2)
    m = [None] * (n1+n2)
    k = 0
    while i < n1 and j < n2:
        if ar1[i] < ar2[j]:
            m[k] = ar1[i]
            i += 1
        else:
            m[k] = ar2[j]
            j += 1
        k += 1
    if i == n1:
        for p in range(j, n2):
            m[k] = ar2[p]
            k += 1
    else:
        for p in range(i, n1):
            m[k] = ar1[p]
            k += 1
    return m
def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr
    else:
        middle = n // 2
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        print("Merging -> ", left, " and ", right, " = ", merge(left, right))
        return merge(left, right)

if __name__ == "__main__":
    arr = [10,16,9,1,8,1,2,4]
    print(merge_sort(arr))
