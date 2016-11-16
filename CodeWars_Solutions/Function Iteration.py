def create_iterator(func, n):
  def result(x):
    func_sum = 0
    for i in range(0,n):
      func_sum = func(x)
      x = func_sum
    return func_sum
  return result

double_iterator = create_iterator(get_double, 2)


class iterator_object:
  def __init__(self, func, n):
    self.func = func
    self.n = n

  def __call__(self, *args):
    n = self.n
    result = self.func(*args)
    while n > 1:
      result = self.func(result)
      n -= 1
    return result

def create_iterator(func, n):
  return iterator_object(func, n)

