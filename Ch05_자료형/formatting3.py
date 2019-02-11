print('{} and {}'.format('King','Queen'))
# 위의 예제와 동일한 결과
print('{0} and {1}'.format('King','Queen'))
# 인수의 순서가 바뀜 {1}은 두번째 인수, {0}은 첫번째 인수
print('{1} and {0}'.format('King','Queen'))

# 인수의 이름을 통해 접근하는 것도 가능함
print('Coordinates: {latitude}, {longitude}'.format(
    latitude='37.24N', longitude='-115.81W'))

print('{:<30}'.format('왼쪽 정렬'))  # 30은 필드의 폭
print('{:>30}'.format('오른쪽 정렬'))


print('{:+f}, {:+f}'.format(3.14, -3.14)) #+,-부호 삽입
print('{: f}, {: f}'.format(3.14, -3.14)) #-부호만 삽입

# 정수 30을 10진수, 16진수, 8진수, 2진수로 출력
print("int: {0:d}; hex: {0:x}; oct: {0:o}; bin: {0:b}".format(30))
print('{:,}'.format(1234567890)) # 1000단위 쉽표 출력

# 소수점 아래 출력
print('1/3은 {:.2%}'.format(1/3))

# 연/월/일/시 출력하는 방법
import datetime # datetime 모듈을 import 함
d = datetime.datetime(2018, 7, 2, 12, 10, 28)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))