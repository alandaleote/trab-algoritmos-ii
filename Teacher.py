from Person import Person 

class Teacher(Person):
    def __init__(self, name, country, classes=[]):
        super().__init__(self, name, country)
        self.classes = classes
        
