import numpy as np

a = np.array([1, 2, 3, 4])
print('a[0] =',a[0])
print('a[1] =',a[1])
print('a[2] =',a[2])
print('a[3] =',a[3])
print('a[-1] =',a[-1])
print('a[-2] =',a[-2])
print()

print('a[np.array([0, 1])] =',a[np.array([0, 1])])
print('a[np.array([0, 2])] =',a[np.array([0, 2])])
print('a[np.array([0, 3])] =',a[np.array([0, 3])])

print('a[np.array([1, 3])] =',a[np.array([1, 3])])
print('a[np.array([0, 1, 2])] =',a[np.array([0, 1, 2])])
print('a[np.array([0, 1, 3])] =',a[np.array([0, 1, 3])])
print('a[np.array([0, 1, 1, 3])] =',a[np.array([0, 1, 1, 3])])