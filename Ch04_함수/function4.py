# ( a * x^2 ) + ( b * x ) + c = 0
# a != 0 인 x에 관한 2차 방정식, 근의 공식으로 해 구하기
# 매개변수를 사용해서 해를 출력해 봅시다
def get_root(a, b, c):
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    return r1, r2


# 함수 호출시 인자를 상수값을 사용함
# result1, result2를 이용해서 결과값을 반환 받아온다
result1, result2 = get_root(1, 2, -8)
print('해는', result1, '또는', result2)
