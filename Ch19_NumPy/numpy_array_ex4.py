import numpy as np

b = np.arange(0, 6).reshape(3, 2)
print('b =',b)
print('b[0, 0] =', b[0, 0])
print('b[0, 1] =', b[0, 1])
print('b[1, 0] =', b[1, 0])
print('b[1, 1] =', b[1, 1])
# 다음은 오류
#print('b[0, 2] =', b[0, 2])
