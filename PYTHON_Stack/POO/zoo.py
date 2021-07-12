class Animal:
    def __init__(self,name):
        self.name = name
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
    def __init__(self, name):
        super().__init__(name)
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
    def __init__(self, name):
        super().__init__(name)
        self.will_to_talk = 50
    
    def feed(self):
        super().feed()
        self.happyness += 90
        self.will_to_talk += 200
    
    def display_info(self):
        super().display_info()
        print(f"Las ganas de hablar del Papagayo son de {self.will_to_talk}")
    

class Lion(Animal):
    def __init__(self, name):
        super().__init__(name)
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
    def __init__(self, name):
        super().__init__(name)
        self.eager_to_hunt = 500

    def feed(self):
        super().feed()
        self.eager_to_hunt -= 50
    
    def hunt(self):
        self.health -= 100
        self.eager_to_hunt -= 200
        self.happyness += 200

    def display_info(self):
        super().display_info()
        print(f"Las ansias de cazar del tigre son de {self.eager_to_hunt}")


class Zoo(Hyenna):
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
        self.animal_count = 0
    
    def add_Hyenna(self, name):
        self.animals.append( Hyenna(name) )
        exec(f"self.{name}_index = self.animal_count")
        self.animal_count += 1
        return self

    def add_Papagayo(self, name):
        self.animals.append( Papagayo(name) )
        exec(f"self.{name}_index = self.animal_count")
        self.animal_count += 1
        return self

    def add_lion(self, name):
        self.animals.append( Lion(name) )
        exec(f"self.{name}_index = self.animal_count")
        self.animal_count += 1
        return self

    def add_tiger(self, name):
        self.animals.append( Tiger(name) )
        exec(f"self.{name}_index = self.animal_count")
        self.animal_count += 1
        return self

    def feed(self, name):
        #exec(f"self.animals[{name}_index].feed()")
        exec(f"self.animals[self."+f"{name}_index"+"].feed()")
        self.animals[0].feed()
        return self

    def play(self, name):
        exec(f"self.animals[self."+f"{name}_index"+"].play()")
        return self

    def hunt(self, name):
        exec(f"self.animals[self."+f"{name}_index"+"].hunt()")
        return self

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
            print("-"*60)
    
    def add_animals(self):
        print("*"*20,"Agregando animales","*"*20,"\n1. Agregar Hyenna.\n2. Agregar Papagayo.\n3. Agregar León\n4. Agregar Tigre\n5. Mostrar Zoológico\n6.Terminar")
        choice=int(input("Ingrese su opción: "))
        while choice>6 or choice<1:
            choice=int(input("Ingrese su opción: "))
        if choice==5:
            self.print_all_info()
            self.add_animals()
        elif choice==6:
            return None
        a_name = input("Ingreseel nombre del animal: ")
        if choice == 1:
            self.add_Hyenna(a_name)
            self.add_animals()
        elif choice==2:
            self.add_Papagayo(a_name)
            self.add_animals()
        elif choice==3:
            self.add_lion(a_name)
            self.add_animals()
        elif choice==4:
            self.add_tiger(a_name)
            self.add_animals()
        
            
        


zoo1 = Zoo("John's Zoo")
zoo1.add_animals()
zoo1.add_Hyenna("kala") .add_lion("koala") .add_tiger("khan") .add_Papagayo("pepe") .print_all_info()
zoo1.feed("khan") .feed("kala") .feed("pepe") .play("koala") .hunt("khan") .print_all_info()


