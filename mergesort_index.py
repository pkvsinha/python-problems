def merge(A, lo, mid, hi):
  print("merging============== > ")
  print_t(A, lo, mid)
  print_t(A, mid+1, hi)
  print("========================")
  arr = [0] * ((hi-lo) + 1)
  i = lo
  j = mid+1
  k = 0
  while i <= mid and j <= hi:
    if A[i] <= A[j]:
      arr[k] = A[i]
      i += 1
    else:
      arr[k] = A[j]
      j += 1
    k += 1
  if i <= mid:
    for p in range(i, mid+1):
      arr[k] = A[p]
      k += 1
  if j <= hi:
    for p in range(j, hi+1):
      arr[k] = A[p]
      k += 1
  k = lo
  for v in arr:
    A[k] = v
    k += 1
  print(arr)
  print("<============== merging ")
def print_t(A, lo, hi):
  print("[", end=" ")
  for i in range(lo, hi+1):
    print(A[i], ",", end="")
  print("]")

def merge_sort(A, lo, hi):
  print_t(A, lo, hi)
  if lo < hi:
    mid = (lo+hi) // 2
    merge_sort(A, lo, mid)
    merge_sort(A, mid+1, hi)
    merge(A, lo, mid, hi)
A= [3,4,1,2,0,18,3,7,19,5]
# merge_sort(A, 0, len(A) - 1)
merge([1,1], 0, 0, 1)
print(A)