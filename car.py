class Wheel:
    def __init__(self, size):
        self.size = size

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Car:
    def __init__(self, make, model, horsepower, wheels_size):
        self.make = make
        self.model = model
        self.engine = Engine(horsepower)
        self.wheels = [Wheel(wheels_size) for _ in range(4)]

my_car = Car("Porsche", "921", 631 , 20)
print(my_car.make)               # Porsche
print(my_car.model)              # 921
print(my_car.engine.horsepower)  # 631
print(my_car.wheels[0].size)     # 20
