class persona:
    def iniciar(self,nombre):
        self.name=nombre
    def imprimir(self):
        print("Su nombre es", self.name)

persona1=persona()
persona1.iniciar("Pepito")
persona1.imprimir()

#crear la clase alumno con sus atributos de nombre y su nota
#Mostrar los valores de los atributos y el estado de aprobacion (>=4)

class alumno:
    def __init__(self, nombre, nota):
        self.nombre_=nombre
        self.nota_=nota
    
    def imprimir_nota(self):
        print("El nombre del alumno es", self.nombre_)
        print("Su nota es", self.nota_)

    def mostrar_estado(self):
        if self.nota_>=4:
            print("El estado es APROBADO")
        else:
            print("El estado es REPROBADO")

alex = alumno("Alex",6.0)
sebastian = alumno("Sebastian", 6.0)

alex.imprimir_nota()
alex.mostrar_estado()

#****************************************************************************************************************
## Definir una Clase Trabajador, donde se solicite por pantalla el ingreso del nombre y el sueldo del trabajador.
## Definir un método para imprimir el nombre y el sueldo
## Definir un método que dependiendo del sueldo aplique un bono. 
## Si el suledo es mayor a 500 mil entonces no aplica el bono, si el sueldo es menor a 500 aplica un bono del 15% del sueldo
## Se debe imprimir el sueldo total.

class asalariado:
    def __init__(self):
        self.nombre = input("Ingrese el nombre del señor asalariado: ")
        self.sueldo = int(input("ingrese el sueldo mensual: "))

    def imprimir_salario(self):
        print(f"El nombre del trabajador es {self.nombre} y su sueldo mensual es de {self.sueldo}")

    def bono(self):
        if self.sueldo<=500000:
            self.sueldo = int(self.sueldo*1.15)
            print(f"El sueldo con bonificación es de {self.sueldo}")
        else:
            print("El trabajador no aplica para el bono")

trabajador=asalariado()
trabajador.imprimir_salario()
trabajador.bono()


