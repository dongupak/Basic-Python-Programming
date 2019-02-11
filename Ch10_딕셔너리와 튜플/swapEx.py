# 임시변수 temp를 이용한 swap
a = 100
b = 200
print('swap 이전 : a=',a,'b=',b)
temp = a
a = b
b = temp
print('swap 이후 : a=',a,'b=',b)

# 튜플을 사용한 간단한 swap
a = 100
b = 200
print('swap 이전 : a=',a,'b=',b)
a, b = b, a
print('튜플을 사용한 swap 결과 : a=',a,'b=',b)
