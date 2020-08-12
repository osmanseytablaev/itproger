class Car:
    колеса = 4
    модель = "Some"
    скорость = 125
    def clon(clon, колеса, скорость, модель):
        clon.колеса = колеса
        clon.скорость = скорость
        clon.модель = модель
    def hi(clon):
        print(clon.колеса, clon.скорость, clon.модель)
Bmv = Car()
Bmv.clon(4, 125.4, "Bmv")
Bmv.hi()

Audi = Car()
Audi.clon(4, 95, "Audi")
Audi.hi()