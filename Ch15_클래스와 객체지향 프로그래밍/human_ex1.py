class Human:
    # 객체의 초기화를 담당하는 생성자
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("이름 :", self.name, " 나이 :", self.age)

    def call(self):
        print(self.name, "를 호출합니다.")


person = Human("수지", 23)
person.info()
person.call()
guy = Human("홍길동", 27)
guy.info()
guy.call()

