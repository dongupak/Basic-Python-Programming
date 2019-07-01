class Person:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):

    def __init__(self, firstname, lastname, staffId):
        Person.__init__(self, firstname, lastname)
        self.staffId = staffId

    def info(self):
        return "Employee : " + self.name() + ", " \
               + str(self.staffId)

class Employer(Person):

    def __init__(self, firstname, lastname, position):
        Person.__init__(self, firstname, lastname)
        self.position = position

    def info(self):
        return "Employer : " + self.name() + ", " \
               + self.position


worker = Employee("Sherlock","Gmones",1111)
cfo = Employer("James","Kim","CFO")

print(worker.info())
print(cfo.info())
