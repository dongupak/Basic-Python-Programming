class Circle:
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius
        self.PI = 3.14

    #  현재 인스턴스의 PI에 반지름**2 을 곱하여 면적을 구함
    def area(self):
        return self.PI * self.radius ** 2


c1 = Circle("C1",4)
print("c1의 면적:",c1.area())
c2 = Circle("C2",6)
print("c2의 면적:",c2.area())
c3 = Circle("C3",5)
# c3.PI = 3.1415
print("c3의 면적:",c3.area())
