def max_path(a, k):
  n = len(a)
  paths = [0] * n
  paths[n-1] = a[n-1]
  for i in range(n-2, -1, -1):
    curr = a[i]
    if (i + 1) < n:
      max_val = curr + paths[i+1]
    else:
      max_val = curr
    for j in range(2, k+1):
      if (i + j) < n:
        max_val = max(curr+paths[j], max_val)
      else:
        break
    paths[i] = max_val
  return paths[0]
print(max_path([1,2,3,4,5,6,7], 3))
print(max_path([20,-10,-5], 2))