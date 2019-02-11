import math

print("math 모듈의 함수들 목록 ")
print(dir(math))

print("math.pow(3,3)=",math.pow(3,3))  # 3의 3승

print("math.fabs(-99)=",math.fabs(-99)) # -99의 절대값
print("math.ceil(2.1)=",math.ceil(2.1)) # 2.1의 올림정수
print("math.ceil(-2.1)=",math.ceil(-2.1))  # -2.1의 올림정수
print("math.floor(2.1)=",math.floor(2.1)) # 2.1의 내림정수
print("math.floor(2.99)=",math.floor(2.99)) # 2.99의 내림정수

print("math.log(2.71828)=",math.log(2.71828))  # e를 밑으로 하는 로그 2.71828
print("math.log(100,10)=",math.log(100,10)) # 10을 밑으로 하는 로그 100

print("math.pi=",math.pi) # pi값 출력
print("math.radians(90)=",math.radians(90))  # 90도를 라디안 값으로 변환시킴

print("math.sin(90.0)=",math.sin(90.0)) # sin(90.0), 사인함수는 라디안 값을 매개변수로 함
print("math.sin(0.0)=",math.sin(0.0))  # sin(0.0)
print("math.sin(3.14159/2.0)=",math.sin(3.14159/2.0)) # sin(pi/2.0)의 근사
print("math.sin(math.pi/2.0)=",math.sin(math.pi/2.0)) # sin(pi/2.0)
print("math.asin(1.0)=",math.asin(1.0)) # sin(pi/2.0)의 역함수
# sin(pi/2.0)의 역함수의 결과가 라디안으로 나오는데 이를 각도값으로 바꾸어 본다
print("math.degrees(math.asin(1.0))=",math.degrees(math.asin(1.0)))
print("math.tan(2*math.pi)=",math.tan(2*math.pi)) # tan(360) 값
print("math.tan(0.0)=",math.tan(0.0)) # tan(0.0) 값

