# 리스트가 iterable 객체인가 검사
try:
    l = [1,2,3,4]
    iterator = iter(l)
except TypeError:
    print('list는 iterable 객체가 아닙니다')
else:
    print('list는 iterable 객체입나다')

# tuple이 iterable 객체인가 검사
try:
    t = ('홍길동',22,69.7)
    iterator = iter(t)
except TypeError:
    print('tuple은 iterable 객체가 아닙니다')
else:
    print('tuple은 iterable 객체입니다')

# tuple이 iterable 객체인가 검사
try:
    n = 100
    iterator = iter(n)
except TypeError:
    print('n은 iterable 객체가 아닙니다')
else:
    print('n은 iterable 객체입니다')

