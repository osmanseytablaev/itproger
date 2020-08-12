class Car:
    wheels = 4
    model = "Some"
    speed = 123.5
    def __init__(self, wheels, model, speed):
        self.wheels = wheels
        self.model = model
        self.speed = speed
    def getAll (self):
            print ("Транспорт ", self.model, " может ехать со скоростью ", self.speed, " на всех ", self.wheels, " колесах!")
Bmv = Car(4, "Bmv", 123.5)
Bmv.getAll()

Mersedes = Car(4, "Mersedes", 143.5)
Mersedes.getAll()