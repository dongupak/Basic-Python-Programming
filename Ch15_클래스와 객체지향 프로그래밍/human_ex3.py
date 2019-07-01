class Human:
    # 객체의 초기화를 담당하는 생성자
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("이름 :", self.name, " 나이 :", self.age)


suji = Human("수지", 23)
suji.age = -100   # 객체 person의 age에 자유롭게 접근하여 문제가 생김
print("suji의 속성값들 :",suji.__dict__)
suji.info()

