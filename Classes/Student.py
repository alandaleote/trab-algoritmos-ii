from Person import Person 

class Student(Person):
    def __init__(self, id, name, country, module):
        super().__init__(self, id, name, country)
        self.module = module
        

