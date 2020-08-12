class Car:
    wheels = 4
    model = "Some"
    speed = 123.5
    def __init__(self, wheels, model, speed):
        self.wheels = wheels
        self.model = model
        self.speed = speed
    def set(self, wheels, model, speed):
        self.wheels = wheels
        self.model = model
        self.speed = speed
    def getAll (self):
        self.__protected ()
    def __protected (self):
        print ("Транспорт ", self.model, " может ехать со скоростью ", self.speed, " на всех ", self.wheels, " колесах!")
class Motorcycle (Car):
    engine = "Default"
    def __init__(self, wheels, model, speed, engine):
        self.engine = engine
        super().__init__(wheels, model, speed)
    def getAll(self):
        super().getAll()
        print ("Его двигатель:", self.engine)
    def change (self, engine):
        self.engine = engine
        print ("Двигатель мотоцикла установлен как: " + engine)	
shkoda = Car (4, "Shkoda", 125.45)
shkoda.getAll ()

audi = Car (4, "Audi", 250.9)
audi.getAll ()

print ("") # Просто пропуск строки

harley = Motorcycle(2, "Harley Davidson", 200, "Powerfull")
harley.getAll ()