from Person import Person 

class Student(Person):
    def __init__(self,name = None, country = None, module = None):
        Person.__init__(self, name, country)
        self.id = None
        self.module = module
        
        
