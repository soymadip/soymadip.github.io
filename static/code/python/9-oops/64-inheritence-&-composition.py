#

# Inheritance is inheriting a parent class. (child class is parent class)
class Animal:
    def speak(self):
        print("Some animal sound")


class Dog(Animal):  # Dog inherits Animal, Dog is an Animal
    def speak(self):
        print("Woof!")


dog = Dog()
dog.speak()  # woof!
#

#
# Composition is creating complex types by combining objects of other types (class has a other class)
class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()  # Composition - The car has an engine, Car is not an engine

    def drive(self):
        self.engine.start()
        print("Car is moving")


car = Car()
car.drive()  # Engine started\n Engine moving


#
#
# ----------------------------------------------------
class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai....")


class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardamom, ginger, cloves.")


class ChaiShop:
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()


class FancyChaiShop(ChaiShop):
    chai_cls = (
        MasalaChai  # overriding chaishop's chai_cls with MasalaChai instead of Basechai
    )


shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai.add_spices()
