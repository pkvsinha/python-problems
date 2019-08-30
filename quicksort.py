def quick_sort(A, lo, hi):
  if lo < hi:
    print(f"====== {lo} - {hi} ======")
    print([0,1,2,3,4,5])
    p = partition(A, lo, hi)
    print("===========================")
    quick_sort(A, lo, p - 1)
    quick_sort(A, p + 1, hi)

def partition(A, lo, hi):
  p =  A[hi]
  i = lo -1
  for j in range(lo, hi):
    if A[j] < p:
      i += 1
      A[j], A[i] = A[i], A[j]
      print(A)
  A[i+1],A[hi] = A[hi],A[i+1]
  return i + 1

arr = [3, 8, 1, 2, 3, 4]
quick_sort(arr, 0, len(arr)-1)
print(arr)