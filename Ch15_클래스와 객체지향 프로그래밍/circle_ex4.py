class Circle:
    PI = 3.14

    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

    # Circle 클래스의 변수 PI를 이용하여 면적을 구함
    def area(self):
        return Circle.PI * self.radius ** 2

c1 = Circle("C1",4)
print("c1의 속성들:", c1.__dict__)
print("Circle 클래스의 속성들:", Circle.__dict__)

