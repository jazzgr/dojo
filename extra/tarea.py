def rut_checker(rut):#Esta funcion saca el digito verificador a partir de la formula linkeada anteriormente
    reversa = map(int, reversed(str(rut))) 
    serie = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversa, serie))
    return (-s) % 11
def store_dictionary(diccionario): #Esta función comprueba el diccionario, pone un nombre al archivo .pkl y crea el archivo pkl
#esta funcion debe comprobar si dict es de tipo diccionario / assert
    assert (type(diccionario) == dict)
    #nombre del archivo dictionary.pkl
    print('sugerencia de nombre del archivo "dictionary"')
    nom = input('Qué nombre desea ponerle al archivo pkl: ')
    #creacion de el archivo pkl
    with open(f"{nom}.pkl", "wb") as tf:
        pickle.dump(diccionario,tf)

    #debe imprimir un comentario como 
    print(f'El diccionario ha sido almacenado como {nom}')

from itertools import cycle
from datetime import datetime
import pickle


#DEFINICIÓN DE VARIABLES
answer = 0
rut = 0 
#df = 0
verificar = 0
nombre = ""
apellido = ""
fechnac = 0 
direc = ""

#Bucle infinito preguntar sucesivamente al usuario por su rut y el bucle termina si el usuario introduce la palabra QUIT
while True:
    answer = input('Desea Corroborar su rut? YES or QUIT= ').upper()
    if answer == 'QUIT':
        print("Usted a decidido salir, Adios")
        break
    else:
        rut = input('Escribe tu rut sin digito verificador= ')
        dg = input('Escribe tu digito verificador si es K ingrese 10 = ')
        rut_checker(rut)
   
    # imprime el rut del usuario
    if dg == '10':
        print(f"Tu rut es: {rut}-k")
    else:
        print(f"Tu rut es: {rut}-{dg}")
    
    
    #verificacion de rut 

    if int(dg) == rut_checker(rut):
        print('Se ha validado con exito su rut,\n le haremos las siguientes pregunta')
        nombre = input('Ingrese su nombre: ')
        apellido = input('Ingrese su apellido: ')
        fechaNac = input('Ingrese su fecha de nacimiento "dd/mm/aaaa": ')
        direc = input('Ingrese su Direccion: ')

        #Diccionario
        chilean_people = {
            'PERSONA': {}
        }
        
        #Agregar rut 
        chilean_people['PERSONA']['RUT'] = rut
        #Agregar al diccionario dicrut
        chilean_people['PERSONA']['nombre'] = nombre
        chilean_people['PERSONA']['apellido'] = apellido
        chilean_people['PERSONA']['fecha nacimiento'] = fechaNac
        chilean_people['PERSONA']['direc'] = direc
        print(chilean_people)

        #almacenar el diccionario 
        store_dictionary(chilean_people)
        #cargar diccionario
    else:
        print('Su rut es incorrecto\n intentelo otra vez')