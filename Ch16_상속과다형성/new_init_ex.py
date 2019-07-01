class Circle :

    def __new__(self):
        print("Circle의 __new__() 메소드 호출")
        return Circle

    def __init__(self, radius):
        self.radius = radius
        print("Circle의 __init__() 메소드 호출")


c = Circle() # A의 __new__() 메소드를 호출
print(c)