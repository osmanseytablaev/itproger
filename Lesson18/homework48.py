class Car: # Создание класса
    wheels = 4 # Несколько полей
    model = "Some"
    speed = 123.5
    def set(self, wheels, model, speed): # Метод для установки значений
        self.wheels = wheels
        self.model = model
        self.speed = speed
    def getAll (self): # Метод для вывода значений
        print ("Автомобиль ", self.model, " может ехать со скоростью ", self.speed, " на всех ", self.wheels, " колесах!")
        pass
class Bike(Car):
    Engine = "Nice"
    def change(self, Engine):
        self.Engine = Engine
        print("Двигатель ", Engine)
Bmv = Car()
Bmv.set(4, "Bmv", 125)
Bmv.getAll() 

Audi = Car()
Audi.set(4, "Audi", 110)
Audi.getAll()

Clon = Bike()
Clon.set(2, "Clon", 269)
Clon.getAll()
   
   