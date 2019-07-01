class Human:
    # 객체의 초기화를 담당하는 생성자
    def __init__(self, name, age):
        self._name = name # 인스턴스 메소드를 감추는 기능
        self._age = age

    def info(self):
        print("이름 :", self._name, " 나이 :", self._age)


suji = Human("수지", 23)
# 다음은 에러 : person 클래스의 __age 인스턴스 변수에 접근이 안됨
print("suji의 속성값들 :",suji.__dict__)
#print(suji._Human__age)
suji.info()    # person 클래스의 메소드는 __age 변수에 접근 가능
