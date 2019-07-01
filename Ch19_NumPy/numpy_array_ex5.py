import numpy as np

c = np.arange(0, 24).reshape(4, 3, 2)
print('c =',c)
print('c[0, 0, 0] =', c[0, 0, 0])
print('c[0, 0, 1] =', c[0, 0, 1])
print('c[0, 1, 0] =', c[0, 1, 0])
print('c[1, 1, 0] =', c[1, 1, 0])
print('c[1, 1, 1] =', c[1, 1, 1])
print('c[1, 2, 1] =', c[1, 2, 1])
print('c[0]=',c[0])
print('c[0, 0] =', c[0, 0])
print('c[1, 0] =', c[0, 1])