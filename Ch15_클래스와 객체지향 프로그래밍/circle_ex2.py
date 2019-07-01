class Circle:
    PI = 3.1415 # 클래스 변수
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

    # Circle 클래스의 변수 PI를 이용하여 면적을 구함
    def area(self):
        return Circle.PI * self.radius ** 2


c1 = Circle("C1",4)
print("c1의 면적:",c1.area())
c2 = Circle("C2",6)
print("c2의 면적:",c2.area())
c3 = Circle("C3",5)
print("c3의 면적:",c3.area())
