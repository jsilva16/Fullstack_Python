class Animal:
    def __init__(self):
        self.name = input("Ingrese el nombre del animal: ")
        self.age = int(input("Ingrese la edad del animal: "))
        self.health = int(input("Ingrese la salud del animal: "))
        self.happyness = int(input("Ingrese la felicidad del animal: "))

    def display_info(self):
        print("El nombre del animal es", self.name)
        print(f"{self.name} tiene {self.age} años de edad.")
        print(f"Su estado de salud es de {self.health} puntos.")
        print(f"Su estado de felicidad es de {self.happyness} puntos.")

    def feed(self):
        self.health += 100
        self.happyness += 10
    
    def play(self):
        self.health -= 50
        self.happyness += 100


class Hyenna(Animal):
    def __init__(self):
        super().__init__()
        self.bloodthirst = 1000
    
    def feed(self):
        super().feed()
        self.health -= 50
        self.happyness += 40
        self.bloodthirst -= 200
    
    def display_info(self):
        super().display_info()
        print(f"La sed de sangre del animal es de {self.bloodthirst}")

class Papagayo(Animal):
    def __init__(self):
        super().__init__()
        self.will_to_talk = 50
    
    def feed(self):
        super().feed()
        self.happyness += 90
        self.will_to_talk += 200
    
    def display_info(self):
        super().display_info()
        print(f"Las ganas de hablar del Ppagayo son de {self.will_to_talk}")
    

class Lion(Animal):
    def __init__(self):
        super().__init__()
        self.lazyness = 50

    def feed(self):
        super().feed()
        self.health -= 80
        self.lazyness += 50
    
    def play(self):
        super().play()
        self.lazyness += 100

    def display_info(self):
        super().display_info()
        print(f"La flojera del león es de {self.lazyness}")
        
class Tiger(Animal):
    def __init__(self):
        super().__init__()
        self.eager_to_hunt = 500

    def feed(self):
        super().feed()
        self.eager_to_hunt -= 50
    
    def hunt(self):



animal1= Hyenna()
animal1.feed()


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_lion(self, name):
        self.animals.append( Lion(name) )
    def add_tiger(self, name):
        self.animals.append( Tiger(name) )
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()


zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.print_all_info()