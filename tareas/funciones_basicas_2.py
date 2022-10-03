#Cuenta Regresiva
def cuenta_regresiva(x):
    lista = []
    for x in range(x,-1,-1):
        lista.append(x)
    print(lista)
    
print(cuenta_regresiva(5))

#imprimir y devolver , funcion que reciba un alista con dos numeros imprie el primer valor y devuleve el segundo, ejemplo 
#impriimr([1,2])ndebe imprimir 1 y devolver 2
lista_imprimir = [1,2]

def imprimir_devolver(list):
    print('imprime',list[0])
    return list[1]
    # for i in range(lista.len):
    #     num1 = lista[i]

print(imprimir_devolver(lista_imprimir))

#Primero mas longitud, crea una funcion que acepte una lista y devuleva la suma del primer valor de la lista, mas la longitud de la lista, ejemplo, [1,2,3,4,5] debe devolver 6(primer valor:1+length: 5)
lista_primero= [1,2,3,4,5]

def primero_longitud(list):
    suma = 0
    suma = len(list) + list[0]
    print(suma)


print(primero_longitud(lista_primero))

#Valores mayores que el segundo, Funcion que acepte una lista y creee una nueva que contenga solo los valores de la lista original que seaa mayores que su segunndo valor, imprime cúantos valores son y luego devuelve la lista nueva, si la funcion tiene menos de dos elementos que devuelva false

lista_mayor = [5,2,3,2,1,4]
lista_corta = [3]

def valores_mayores(lista):
    lista_nueva = []
    if len(lista) < 2:
        return False
    
    for i in range (0, len(lista)):
        if lista[i] > lista[1]:
            lista_nueva.append(lista[i])
    print(len(lista_nueva))
    return lista_nueva    

print(valores_mayores(lista_mayor))
print(valores_mayores(lista_corta))

#Esta longitud, ese valor: escribe una función que acepte dos enteros como parámetros: tamaño y valor. La función debe crear y devolver una lista cuya longitud sea igual al tamaño dado, y cuyos valores sean todos el valor dado. Ejemplo: length_and_value(4,7) debe devolver [7,7,7,7] Ejemplo: length_and_value(6,2) debe devolver [2,2,2,2,2,2]
    
def longitud(tamano, valor):
    lista_longitud = []
    for i in range(0, tamano):
        lista_longitud.append(valor)
    return lista_longitud

print(longitud(4,7))
print(longitud(6,2))