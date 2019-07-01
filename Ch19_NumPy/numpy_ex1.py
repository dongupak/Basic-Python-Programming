import numpy as np

a = np.array([1, 2, 3])
print('a =', a)
print('type(a) = ',type(a))
b = np.array([4, 5, 6])
print('b =', b)

c = a + b
print('c =', c)
print('c.shape =', c.shape)
print('c.size =', c.size)
print('c.itemsize =', c.itemsize)

d = np.array([2, 4, 6, 8, 10])
print('d =', d)
print('d.shape =', d.shape)
print('d.size =', d.size)
print('d.itemsize =', d.itemsize)


