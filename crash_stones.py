def nextPair(a, i, j):
  lj = j - 1
  if lj >= 0:
    if a[lj] == 0:
      return nextPair(a, j, lj)
    if a[lj] > a[i]:
      return (j, lj)
    else:
      return (i, j)
  return (i, j)

def crashStones(a):
  i = len(a) - 1
  j = i - 1
  while j >= 0:
    if a[i] == 0:
      i = j
      j -= 1
      continue
    if a[j] == 0:
      j -= 1
      continue
    if a[i] == a[j]:
      a[i] = 0
      a[j] = 0
      i -= 2
      j -= 2
    elif a[i] > a[j]:
      a[i] -= a[j]
      a[j] = 0
      j -= 1
      i, j = nextPair(a, i, j)
    else:
      a[j] -= a[i]
      a[i] = 0
      i = j
      j -= 1
      i, j = nextPair(a, i, j)
  rem = []
  for e in a:
    if e > 0:
      rem.append(e)
  return rem

def job(a):
  rem = a
  while len(rem) > 1:
    rem.sort()
    rem = crashStones(rem)
  if len(rem) == 0:
    return 0
  else:
    for e in rem:
      if e > 0:
        return e
print(job([1,2,3,5,7,9]))
print(job([46188086,
339992587,
742976890,
801915058,
393898202,
717833291,
843435009,
361066046,
884145908,
668431192,
586679703,
792103686,
85425451,
246993674,
134274127,
586374055,
923288873,
292845117,
399188845,
842456591,
410257930,
333998862,
16561419,
624279391,
459765367,
969764608,
508221973,
82956997,
437034793,
553121267,
554066040,
199416087])) # 659075