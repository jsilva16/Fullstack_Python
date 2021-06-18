class BankAccount:
    def __init__(self,int_rate=0.01, balance=0):
        self.saldo = balance
        self.rate = int_rate

    def deposit(self, monto):
        self.saldo = int(self.saldo+monto)
        #print(f"Se han depositado ${monto} en la cuenta del usuario {self.nombre}. Su saldo final es ${self.saldo}.")
        return self

    def display_account_info(self):
        print(f"El saldo en la cuenta del usuario es: ${self.saldo}.")
        return self

    def withdraw(self, retire):
        if self.saldo>=retire:
            self.saldo = int(self.saldo-retire)
            #print(f"Se han retirado ${retire} de la cuenta del usuario {self.nombre}. Su saldo final es ${self.saldo}.")
        else:
            print("Fondos insuficientes: cobrar una tarifa de $ 5")
            self.saldo = self.saldo - 5
        return self


    def yield_interest(self):
        self.saldo = self.saldo*(1+self.rate)
        return self

#Creación de cuentas
cuenta1 = BankAccount(0.2)
cuenta2 = BankAccount(0.02,10000)

#Operaciones
cuenta1.deposit(1000) .deposit(250000) .withdraw(50000) .yield_interest() .display_account_info()
cuenta2.deposit(500000) .deposit(1000) .withdraw(20000) .withdraw(50000) .withdraw(100000) .withdraw(50000) .yield_interest() .display_account_info()

