ages = [34, 39, 20, 18, 13, 54]

print('성년 리스트 :')
# filter 함수를 통과한 내용을 리스트로 만든다
adult_ages = list(filter(lambda x: x >= 19, ages))
print(adult_ages)

