from Person import Person 

class Teacher(Person):
    def __init__(self, name=None, country=None, module=None, weekday=None,):
        Person.__init__(self, name, country)
        self.id = None
        self.module = module
        self.weekday = weekday
        
