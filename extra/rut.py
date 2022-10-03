from itertools import cycle
from datetime import datetime
import pickle

#VARIABLES
condition = 0
answer = 0
rut = 0 
df = 0
verificar = 0
nombre = ""
apellido = ""
fechnac = 0 
direc = ""

#FUNCION
def rut_checker(rut):
    reversa = map(int, reversed(str(rut)))
    serie = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversa, serie))
    return (-s) % 11

def store_dictionary(dicionario):
    #esta funcion debe comprobar si mdict es de tipo diccionario / assert
    mdict = {}
    #no me funciona el assert
    #assert(dicionario == mdict,'Se comprueba que es un diccionario')
    
    #nombre del archivo dictionary.pkl
    print('sugerencia de nombre del archivo "dictionary"')
    nom = input('Qué nombre desea ponerle al archivo pkl: ')
    #creacion de el archivo pkl
    with open(f"{nom}.pkl", "wb") as tf:
        pickle.dump(dicionario,tf)
    
    #debe imprimir un comentario como 
    print(f'El diccionario ha sido almacenado como {nom}')

    

#Bucle infinito preguntar sucesivamente al usuario por su rut y el bucle termina si el usuario introduce la palabra QUIT

while condition == 0:
    answer = input('Desea Corroborar su rut? YES or QUIT= ').upper()
    if answer == 'QUIT':
        condition = 1
        print("Usted a decidido salir, Adios")
        break
    else:
        rut = input('Escribe tu rut sin digito verificador= ')
        dg = input('Escribe tu digito verificador si es K ingrese 10 = ')
        rut_checker(rut)
    print(f"Tu rut es: {rut}-{dg}")
    #print(rut_checker(rut))
    
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
        




    




