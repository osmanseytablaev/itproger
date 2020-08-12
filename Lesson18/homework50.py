class Car():
    wheels = 4
    model = "Some"
    speed = 134.5
    def hi(self, wheels, model, speed):
        self.wheels = wheels
        self.model = model
        self.speed = speed
    def Bye(self):
        self.__clon()
    def __clon(self):
        print("Автомобиль ", self.model, " может ехать со скоростью ", self.speed, " на всех ", self.wheels, " колесах")