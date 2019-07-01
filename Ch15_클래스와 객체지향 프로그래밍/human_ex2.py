class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "{}(나이 {}세)".format(self.name, self.age)


person = Human('수지', 23)   # 초기화 함수 사용
print(person)

