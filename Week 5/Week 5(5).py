
class Animal:
    def __init__(self, name):
        self.name = name

    def action(self):
        print("Animal performs an action")

# Level 1 
class Mammal(Animal):
    def __init__(self, name, feature):
        super().__init__(name)
        self.feature = feature


class Bird(Animal):
    def __init__(self, name, feature):
        super().__init__(name)
        self.feature = feature


class Fish(Animal):
    def __init__(self, name, feature):
        super().__init__(name)
        self.feature = feature

# Level 2 

class Dog(Mammal):
    def action(self):
        print(f"{self.name} walks on land")


class Cat(Mammal):
    def action(self):
        print(f"{self.name} walks gracefully")


class Eagle(Bird):
    def action(self):
        print(f"{self.name} flies high in the sky")


class Penguin(Bird):
    def action(self):
        print(f"{self.name} swims instead of flying")


class Salmon(Fish):
    def action(self):
        print(f"{self.name} swims upstream")


class Shark(Fish):
    def action(self):
        print(f"{self.name} swims powerfully in the ocean")

# Main Program

animals = [

    Dog("Dog", "warm-blooded"),
    Cat("Cat", "warm-blooded"),
    Eagle("Eagle", "has wings"),
    Penguin("Penguin", "has wings"),
    Salmon("Salmon", "has fins"),
    Shark("Shark", "has fins")
]

# Same method call for all objects
for animal in animals:
    animal.action()

