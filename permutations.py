def permute(a, k):
  n = len(a)
  if n == 0:
    return []
  elif n == 1:
    return [[a[0]]]
  perms = []
  for i in range(n):
    c = a[i]
    sub_perm = permute(a[:i] + a[i+1:], k)
    for p in sub_perm:
      perms.append([c]+p)
  return perms

print(permute(['a','b','c'], 3))