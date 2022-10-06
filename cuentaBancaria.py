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


#!MÉTODOS DE OBJETO/INSTANCIA
    def re_tiro(self,cantidad):
        # podemos usar el método estático aquí para evaluar
        # si podemos retirar los fondos sin quedar con balance negativo
        if CuentaBancaria.puede_retirar(self.balance,cantidad):
            self.balance -= cantidad
        else:
            print("Fondos insuficientes")
        return self 


   

#!MÉTODOS DE CLASE
    # método de clase para cambiar el nombre del banco
    @classmethod
    def cambiar_nombre_banco(cls, name):
        cls.nombre_banco = name

    # método de clase para obtener balance de todas las cuentas
    @classmethod
    def todos_los_balances(cls):
        sum = 0
        # utilizamos cls para referirnos a la clase
        for account in cls.todas_las_cuentas:
            sum += balance.cuenta
        return sum

    @classmethod
    def imprimir_todas_cuentas(cls):
        for cuenta in cls.todas_las_cuentas:
            print(f"Esta cuenta tiene un balance de {cuenta.balance}")
            # print(cuenta.__dict__)

#!MÉTODOS DE ESTATICOS
    # los métodos estáticos no tienen acceso a ningún atributo
    # solo a lo que se le pasa
    @staticmethod
    def puede_retirar(balance,cantidad):
        if (balance - cantidad) < 0:
            return False
        else:
            return True
