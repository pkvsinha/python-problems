class Complex:
  name = 'Complex Type'

  def __init__(self, r, i):
    self.r = r
    self.i = i
    print(self.name)

c = Complex(3.4,-4.5)
print(f'{c.i}+i{c.r}')
print(c.name)