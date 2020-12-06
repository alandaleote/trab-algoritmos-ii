from Person import Person 

class Teacher(Person):
    def __init__(self, name, country, classes=[]):
        Person.__init__(self, name, country)
        self.id = None
        self.classes = classes
        
