class CuentaBancaria:

    banco = "BANCO JAZZ"
    cuentas = []

    def __init__(self, tasa_interes, balance):
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.cuentas.append(self)

    def deposito(self, amount):
        #aumenta el balance de la cuenta en el monto dado
        self.balance = balance + amount
        return self

    def retiro(self, amount):
        
        if self.balance < amount:
            # si no hay suficiente dinero, imprime el mensaje: "Fondos insuficientes: cobrando una tarifa de $5", y resta $5
            self.balance = balance - 5
            print("Fondos insuficientes: cobrando una tarifa de $5")
        else:
            #disminuye el balance de la cuenta en el monto dado si hay fondos suficientes;
            self.balance = balance - amount
        return self

    def mostrar_info_cuenta(self):
        #imprime en la consola: por ejemplo, "Balance: $100"
        print("Balance:$", self.balance)
        return self
    
    def generar_interes(self):
        #(siempre que el balance sea positivo) 
        if self.balance > 0:
            #aumenta el balance de la cuenta por el balance actual * la tasa de interés 
            self.balance = self.balance + (self.balance * self.tasa_interes)  
        return self

