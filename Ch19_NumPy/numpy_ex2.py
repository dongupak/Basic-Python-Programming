import numpy as np

a = np.array([[1, 2], [3, 4]])
print('a =', a)
b = np.array([[10, 20], [30, 40]])
print('b =', b)
print('b.ndim =', b.ndim)

c = a + b
print('c =', c)
d = b - a
print('d =', d)
e = a * b
print('e =', e)

f = np.matmul(a, b)
print('f =', f)
g = a @ b
print('g =', g)