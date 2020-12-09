class Person:

    def __init__(self, name = None, country = None):
        self.name = name
        self.country = country

    def setName(self, name):
    self.name = name

    def getName(self):
        return self.name
    
    def setCountry(self, country):
        self.country = country

    def getCountry(self):
        return self.country
        