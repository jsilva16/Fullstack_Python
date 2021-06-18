#Objeto de cuenta bancaria

class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.saldo = balance
        self.rate = int_rate

    def deposit(self, monto):
        self.saldo = int(self.saldo+monto)

    def display_account_info(self):
        print(f"El saldo en la cuenta del usuario es: ${self.saldo}.")

    def withdraw(self, retire):
        if self.saldo >= retire:
            self.saldo = int(self.saldo-retire)
        else:
            print("Fondos insuficientes: cobrar una tarifa de $ 5")
            self.saldo = self.saldo - 5

    def yield_interest(self):   
        self.saldo = self.saldo*(1+self.rate)


#Objeto de Usuario

class usuario:
    def __init__(self, name):
        #self.nombre = input("Ingrese el nombre del usuario: ")
        self.name = name
        self.account = BankAccount()

    def openAccount(self, account_name):
        exec("self."+account_name+" = BankAccount()")
        print(f"Se ha creado una nueva cuenta a nombre del cliente {self.name}, llamada {account_name}.")

    def deposit(self, monto, account_name="account"):
        exec("self."+account_name+".deposit(monto)")
        print(f"Se han depositado ${monto} en la cuenta {account_name}, del usuario {self.name}.")
        exec("self."+account_name+".display_account_info()")
        return self

    def balance(self, account_name="account"):
        exec("self."+account_name+".display_account_info()")
        return self

    def withdraw(self, retire, account_name="account"):
        exec("self."+account_name+".withdraw(retire)")
        print(
            f"Se han retirado ${retire} de la cuenta del usuario {self.name}.")
        exec("self."+account_name+".display_account_info()")
        return self

    def transfer(self, destino, origen="account", monto=0):
        self.withdraw(monto, origen)
        destino.deposit(monto)
        #exec("self."+origen+".display_account_info()")
        print(f"Se han transferido ${monto} exitosamente a la cuenta del usuario {destino.name}")
        return self

    def yield_interest(self):
        self.account.yield_interest()
        return self


#deficion de las instancias
usuario1 = usuario("Pedro")
usuario2 = usuario("Juan")
usuario3 = usuario("Diego")

#Operaciones Usuario 1
usuario1.openAccount("cuentarut")
usuario1.balance()
usuario1.balance("cuentarut")
usuario1.deposit(5000,"cuentarut")
usuario1.deposit(10000)
usuario1.transfer(usuario2,"cuentarut",100)
usuario1.withdraw(5000)
usuario1.balance()


































class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.monto=0

    def depositar(self, monto):
        self.monto = self.monto+monto
    
    def giro(self,monto):
        self.monto = self.monto-monto

    def devolverMonto(self):
        return self.monto
    
    def imprimirResultado(self):
        print(self.nombre, " Usted tiene un saldo de: ", self.monto)

class Banco:
    def __init__(self):
        self.cliente1 = Cliente("Juanito")
        self.cliente2 = Cliente("Pepito")

    def realizarTransaccion(self):
        self.cliente1.depositar(1000)
        self.cliente2.depositar(10000)
        self.cliente1.giro(500)
        self.cliente2.giro(50000)
    
    def imprimir(self):
        self.cliente1.imprimirResultado()
        self.cliente2.imprimirResultado()

bco = Banco()
bco.realizarTransaccion()
bco.imprimir()
