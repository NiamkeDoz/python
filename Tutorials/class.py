class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age
    
    def printInfo(self):
        print(self.name)
        print(self.age)
    
person1 = Person("Scooter", 25)
person1.printInfo()