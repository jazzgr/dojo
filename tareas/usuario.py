#Crea un archivo con la clase Usuario, incluyendo los métodos __init__ y hacer_depósito

class Usuario:
    banco = "Banco Dojo"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance_cuenta = 0

    def hacer_deposito(self, amount):
        self.balance_cuenta += amount
    
    #: haz que este método reduzca el balance del usuario en la cantidad especificada 
    def hacer_retiro(self, amount):
        self.balance_cuenta -= amount

    #haz que este método imprima el nombre del usuario y el balance de cuenta en la terminal 
    def mostrar_balance_usuario(self):
        print(f"Nombre del Usuario: {self.name}, Balance: {self.balance_cuenta} ")
    
    #haz que este método reduzca el balance del usuario por el monto y agrega esa cantidad al balance de otro_usuario 
    def  transfer_dinero(self, other_user, amount):
        self.hacer_retiro(amount)
        other_user.hacer_deposito(amount)

#Crea 3 instancias de la clase Usuario
jazz = Usuario("jazz", "jazz@gmail.com")
marcelo = Usuario("marcelo", "marcelo@gmail.com")
mayna = Usuario("mayna", "mayna@gmail.com")

#Haz que el primer usuario haga 3 depósitos y 1 giro, y luego muestra sus balances
jazz.hacer_deposito(400)
jazz.hacer_retiro(100)
jazz.mostrar_balance_usuario()

marcelo.hacer_deposito(1000)
marcelo.mostrar_balance_usuario()

marcelo.transfer_dinero(jazz,800)

jazz.mostrar_balance_usuario()
marcelo.mostrar_balance_usuario()