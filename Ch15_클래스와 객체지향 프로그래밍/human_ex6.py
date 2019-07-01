class Human:
    # 객체의 초기화를 담당하는 생성자
    def __init__(self, name, age):
        self.__name = name   # 인스턴스 메소드를 감추는 기능
        self.__age = age

    # 아래와 같이 @property 지시자를 이용하여 외부에서 접근을 허
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 0 :
            self.__age = age
        else :
            self.__age = 0


person = Human("수지", 23)
person.name = "수아"
person.age = -30
print("이름 : ",person.name,"나이 :",person.age)
