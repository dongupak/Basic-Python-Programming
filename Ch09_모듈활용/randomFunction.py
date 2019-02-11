import random

# 0이상 1미만의 실수를 반환한다
print(random.random())

# 1이상 7미만(6까지)의 정수를 반환한다
print(random.randrange(1, 7))

# 0이상 10미만의 임의의 정수중 2의 배수를 반환한다
print(random.randrange(0, 10, 2))

# numlist 리스트내의 원소를 랜덤하게 섞는다
numlist = [1,2,3,4,5]
random.shuffle(numlist)
print(numlist)

# numlist 리스트내의 원소를 랜덤하게 선택한다
print(random.choice(numlist))
# numlist 리스트내의 원소를 랜덤하게 3개 선택한다
print(random.sample(numlist, 3))