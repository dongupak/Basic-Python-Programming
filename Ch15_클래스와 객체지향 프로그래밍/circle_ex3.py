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
# __dic__[key] 형식으로 value를 얻을 수 있음
print("c1의 name 변수값:", c1.__dict__['name'])
print("c1의 radius 변수값:", c1.__dict__['radius'])

