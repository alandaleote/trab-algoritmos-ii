from Person import Person 

class Teacher(Person):
    def __init__(self, id, name, country, classes=[]):
        super().__init__(self, id, name, country)
        self.classes = classes
        
