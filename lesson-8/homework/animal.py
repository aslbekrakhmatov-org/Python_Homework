class animal:
    def __init__(self, name, food):
        self.name = name
        self.food = food

    def __str__(self):
        return f"{self.name} eats {self.food}."

    def task(self):
        return f"Eat and sleep"
        

class Dog(animal):
    def __init__(self, name, food, color):
        super().__init__(name, food)
        self.color = color

    def __str__(self):
        return super().__str__(), f"{self.name} is {self.color}."


    def task(self):
        super().task()
        return f"{super().task()}. Moreover, defends the farm"

class Cow(animal):
    def __init__(self, name, food, weight):
        super().__init__(name, food)
        self.weight = weight
    
    def __str__(self):
        return f"{super().__str__()} and has a {self.weight} weight."
    def task(self):
        return f"{super().task()}. Moreover, gives milk."

class Bird(animal):
    def task(self):
        return f"{super().task()}. Moreover, sings."

animal1 = animal("Sheep", "leaves")
print(animal1)

dog1 = Dog("Max", "bone", "black")
print(dog1.task())

cow1 = Cow("Mosh", "arpa", "150kg")
print(cow1)
print(cow1.task())
bird1 = Bird("Bulbul", "seeds")
print(bird1.task())


