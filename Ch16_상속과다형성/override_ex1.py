class Person:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return self.firstname + " " + self.lastname


class Employee(Person):

    def __init__(self, firstname, lastname, staffId):
        super().__init__(firstname, lastname)
        self.staffId = staffId

    # 부모 클래스의 메소드를 오버라이딩
    def __str__(self):
        return "Employee : " + super().__str__() + ", " \
               + str(self.staffId)


worker = Employee("Sherlock", "Gmones", 1111)
print(worker)