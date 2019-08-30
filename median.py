class Window:

    def __init__(self, size, maxv, arr=[]):
        self.size = size
        self._count = [0] * (maxv + 1)
        for e in arr:
            self._count[e] += 1

    def add(self, n):
        i = 0
        while self._count[i] == 0:
          i += 1
        self._count[i] -= 1
        self._count[n] += 1
        

    def median(self):
        if self.size % 2 == 0:
            mid = (self.size // 2) + 1
            c = 0
            p = None
            i = 0
            for num in self._count:
              if (c + num) >= mid:
                if p == None:
                  return i
                else:
                  return (p + i) / 2
              elif (c + num) == (mid - 1):
                p = i
              c += num
              i += 1
        else:
            mid = ((self.size - 1) // 2 ) + 1
            i = 0
            while mid > 0:
                if self._count[i] == 0:
                    i += 1
                else:
                    if self._count[i] >= mid:
                        return i
                    else:
                        mid -= self._count[i]
                        i += 1
                
window = Window(6, 8, [2,4,6,8,5,4])
print([0,1,2,3,4,5,6])
print(window._count)
window.add(5)
print(window._count)
window.add(8)
print(window._count)
print(window.median())
