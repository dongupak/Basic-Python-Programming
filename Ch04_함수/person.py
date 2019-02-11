# 다중값 반환 함수 - 테스트용
def person_info():
    name = '홍길동'
    age = 27
    position = '왕'
    return name, age, position


p_name, p_age, p_pos = person_info()
print('이름은', p_name, '나이는', p_age, '직책은', p_pos)
