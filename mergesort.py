def merge(a, b):
  print("merge", a, b)
  if len(a) == 0:
    return b
  if len(b) == 0:
    return a
  m = len(a)
  n = len(b)
  arr = [0] * (m+n)
  for i, v in enumerate(a):
    arr[i] = v
  i = m
  for v in b:
    j = i
    while j > 0 and arr[j - 1] > v:
      arr[j] = arr[j-1]
      j -= 1
    i += 1
    arr[j] = v
  print("merging=> ", a, "and", b, " = ", arr)
  return arr

def merge_sort(A):
  print(A)
  if len(A) == 1:
    return A
  mid = len(A) // 2
  a = merge_sort(A[:mid])
  b = merge_sort(A[mid:])
  return merge(a, b)

print(merge_sort([1,2,3,10,120,5,6,72,8]))
# print(merge([120],[5]))