# fruits 딕셔너리의 생성
fruits = {'melon':300, 'banana':500, 'orange':700}

print(fruits.keys())  # fruits 딕셔너리의 key 값들을 출력
print(fruits.values())# fruits 딕셔너리의 value 값들을 출력
print('apple' in fruits.keys()) # in 연산자 사용
print('banana' in fruits.keys())
print(fruits.items())

# 새로운 딕셔너리 생성
new_fruits = {'watermelon':400, 'peach':800, 'mango':600}
fruits.update(new_fruits) # 새 딕셔너리를 기존 딕셔너리에 합친다
print(fruits.items())
del(fruits['peach'])  # 'peach' 키를 가지는 아이템을 삭제한다
print(fruits.items())
fruits.clear()  # 딕셔너리의 모든 원소를 삭제함
print(fruits.items())

