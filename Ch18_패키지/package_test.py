import sys
sys.path.append("/Users/dongupak/pkgTutorial")
# 위의 작업 디렉토리 경로는 개발자마다 다를 수 있습니다.
# 특히 윈도 컴퓨터의 경우 C:\Users\user-id 와 같은 형식으로 수정해야 함

import math_pkg.math_op
print('100 + 200 =', math_pkg.math_op.add(100, 200))

import str_pkg.str_op
print(str_pkg.str_op.upper('hello'))



