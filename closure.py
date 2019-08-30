def swap_with_count():
  count = 0
  def swap(arr=None, i=None, j=None):
    nonlocal count
    if arr == None:
      return count
    else:
      t = arr[i]
      arr[i] = arr[j]
      arr[j] = t
      count += 1
  return swap
counter =  swap_with_count()
arr = [3,2,1]
counter(arr, 0, 1)
counter(arr, 1, 2)
counter(arr, 0, 1)
print(arr)
print(counter())

def counter_fn():
    count = 0
    def inc(i=None):
        nonlocal count
        if i == None:
            return count
        count += i
    return inc
inc = counter_fn()
inc(1)
inc(10)
print(inc ())