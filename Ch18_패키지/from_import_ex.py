import sys
sys.path.append("/Users/dongupak/pkgTutorial")

from math_pkg import math_op
print('100 + 200 =', math_op.add(100,200))

from str_pkg import str_op
print(str_op.upper('hello'))


