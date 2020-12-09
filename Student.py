from Person import Person 

class Student(Person):
    def __init__(self,name=None, country=None, module=None, weekday=None):
        Person.__init__(self, name, country)
        self.id = None
        self.module = module
        self.weekday = weekday
    
    def setModule(self, module):
        self.module = module

    def getModule(self):
        return self.odule
    
    def setWeekday(self, weekday):
        self.weekday = weekday

    def getWeekday(self):
        return self.weekday
    
        

