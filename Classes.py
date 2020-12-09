
class Classes:

    def __init__(self, module=None, weekday=None, teachername=None):
        self.id = id 
        self.module = module
        self.weekday = weekday
        self.teachername = teachername
    
    def setModule(self, module):
        self.module = module

    def getModule(self):
        return self.odule
    
    def setWeekday(self, weekday):
        self.weekday = weekday

    def getWeekday(self):
        return self.weekday

    def setTeachername(self, teachername):
        self.teachername = teachername

    def getTeachername(self):
        return self.teachername
    
