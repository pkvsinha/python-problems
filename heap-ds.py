
class Heap:

  def __init__(self, arr):
    self._arr = arr
    N = len(arr)
    for i in range(N//2, -1, -1):
      self._max_heap(arr, i, N)

  def _max_heap(self, arr, i, N):
    left = 2 * i
    right = (2 * i) + 1
    largest = i
    if left < N and arr[left] > arr[i]:
      largest = left
    if right < N and arr[right] > arr[largest]:
      largest = right
    if largest != i:
      arr[largest], arr[i] = arr[i], arr[largest]
      self._max_heap(arr, largest, N)

  def find_max(self):
    return self._arr[0]
  
  def sort(self):
    sorted_arr = [e for e in self._arr]
    N = len(self._arr)
    for i in range(N//2, -1, -1):
      sorted_arr[i], sorted_arr[0] = sorted_arr[0], sorted_arr[i]
      N -= 1
      self._max_heap(sorted_arr, 0, N)
    return sorted_arr

  def insert(self):
    pass

  def delete(self):
    pass


heap = Heap([4,1,21,9,10])
print(heap.sort())
  