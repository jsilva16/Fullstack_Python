# Definir clase persona

class Persona:
    def __init__(self):
        self.nombre = input("Ingrese su nombre: ")
        self.edad = int(input("Ingrese la edad: "))
    
    def mostrarDatos(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)


#definiendo clase Trabajador

class Trabajador(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = int(input("Ingrese el sueldo: "))

    def mostrarDatos(self):
        super().mostrarDatos()
        print("Sueldo: ", self.sueldo)
    
    def agregarBono(self):
        if self.sueldo<700000:
            print("El trabajador recibirá un bono del 10% sobre su sueldo")
        else:
            print("Siga participando")

persona1= Persona()
persona1.mostrarDatos()
print("****************************")
trabaja1 = Trabajador()
trabaja1.mostrarDatos()
trabaja1.agregarBono()