class Human:
    # 객체의 초기화를 담당하는 생성자
    def __init__(self, name, age):
        self.__name = name  # 인스턴스 메소드를 감추는 기능
        self.__age = age

    def info(self):
        print("이름 :", self.__name, " 나이 :", self.__age)


suji = Human("수지", 23)
print("suji의 속성값들 1:",suji.__dict__)
# 아래의 경우 suji 인스턴스 변수 __age를 생성
suji.__age = 100
print("suji의 속성값들 2:",suji.__dict__)

minsu = Human("민수", 24)
print("민수의 속성값들",minsu.__dict__)

