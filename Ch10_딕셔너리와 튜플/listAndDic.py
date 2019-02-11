list = [11, 22, 33, 44, 55, 66]
print(list)
print('list[1]=',list[1])
list.pop(0)
print(list)
print('list[1]=',list[1])

dic = {0:11, 1:22, 2:33, 3:44, 4:66}
# 딕셔너리의 (키,값) 튜플쌍을 반환하는 items() 함수
print(dic.items())
print('dic[1]=',dic[1])
dic.pop(0)
print(dic.items())
print('dic[1]=',dic[1])


