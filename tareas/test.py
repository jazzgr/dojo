from cuentaBancaria import CuentaBancaria

cuenta1 = CuentaBancaria(0.15, 100)
# print("Balance previo al deposito",cuenta1.balance)
cuenta1.deposito(300).mostrar_info_cuenta()
# print("Balance despues al deposito",cuenta1.balance)
cuenta1.retiro(400).mostrar_info_cuenta()
cuenta1.generar_interes().mostrar_info_cuenta()
# print("Balance actual",cuenta1.balance)

cuenta2 = CuentaBancaria(0.15, 50)

# print(CuentaBancaria.todas_las_cuentas)
CuentaBancaria.imprimir_todas_cuentas()
