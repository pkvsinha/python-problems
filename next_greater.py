def next_greater(a):
  n = len(a)
  greater_arr = [None] * n
  stack = []
  stack.append(a[0])
  for i in range(1, n):
    if 

  return greater_arr

print(next_greater([8,2,3,5,6,7]))