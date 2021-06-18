class usuario:
    def __init__(self,nombre):
        #self.nombre = input("Ingrese el nombre del usuario: ")
        self.nombre = nombre
        self.saldo = 0

    
    def deposit(self, monto):
        self.saldo = int(self.saldo+monto)
        print(f"Se han depositado ${monto} en la cuenta del usuario {self.nombre}. Su saldo final es ${self.saldo}.")
        return self

    def balance(self):
        print(f"El saldo en la cuenta del usuario {self.nombre} es: ${self.saldo}.")
        return self

    def withdraw(self, retire):
        if self.saldo>=retire:
            self.saldo = int(self.saldo-retire)
            print(f"Se han retirado ${retire} de la cuenta del usuario {self.nombre}. Su saldo final es ${self.saldo}.")
        else:
            print("El saldo en la cuenta es insuficiente")
        return self
    
    def transfer(self, destino, monto):
        if self.saldo>=monto:
            self.saldo= self.saldo-monto
            self.balance()
            destino.deposit(monto)
        else:
            print("El saldo en la cuenta es insuficiente para realizar esta transacción.")
        print(f"Se han transferido ${monto} exitosamente a la cuenta del usuario {destino.nombre}")
        self.balance()
        destino.balance()
        return self


#deficion de las instancias
usuario1 = usuario("Pedro")
usuario2 = usuario("Juan")
usuario3 = usuario("Diego")

#Operaciones Usuario 1
usuario1.balance() .deposit(5000) .deposit(10000) .deposit(15000) .withdraw(5000) .balance()

#Operaciones Usuario 2
usuario2.deposit(5000) .deposit(10000) .withdraw(5000) .withdraw(150000) .balance()

#Operaciones Usuario 3
usuario3.deposit(500000) .withdraw(10000) .withdraw(5000) .withdraw(150000) .balance()

#BONUS
usuario1.transfer(usuario3, 5000)