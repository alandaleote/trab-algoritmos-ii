from Person import Person 

class Teacher(Person):
    def __init__(self, name, country, module, weekday,):
        Person.__init__(self, name, country)
        self.id = None
        self.module = module
        self.weekday = weekday
        
