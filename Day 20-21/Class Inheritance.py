class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale. ")

class Fish(Animal):
    def __init__(self):
        super().__init__() # refers to (Animal) class

    def breathe(self):
        super().breathe()
        print("Doing it underwater. ")

    def swim(self):
        print("Moving in water")

nemo = Fish()
nemo.breathe()