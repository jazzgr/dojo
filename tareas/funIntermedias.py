x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'futbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


#Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
x[1][0] = 15
#Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
estudiantes[0]['last_name'] = 'Bryan'
#En el directorio_deportes, cambia "Messi" por "Andrés".
directorio_deportes['futbol'][0] = 'Andrés'
#Cambia el valor 20 en z a 30.
z[0]['y']= 30

print(x)
print(estudiantes)
print(directorio_deportes)
print(z)

#Iterar a través de una lista de diccionarios Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios,

estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


''' debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
un bonus para que aparezcan exactamente como se muestra a continuación)
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel'''

def iterateDictionary(some_list):
    print(' ------')
    for i in some_list:
        print(f'{i}')
    

iterateDictionary(estudiantes)


# Obtener valores de una lista de diccionarios
# Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, la función imprima el valor almacenado en esa clave para cada diccionario. Por ejemplo, iterateDictionary2('name', estudiantes) debería generar

estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(key_name, some_list):
    print(' ------')
    for i in some_list:
        print(i[key_name])

iterateDictionary2('first_name', estudiantes)
iterateDictionary2('last_name', estudiantes) 

# Iterar a través de un diccionarios con valores de lista
# Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todos listas, imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores asociados dentro de la lista de cada clave. Por ejemplo:


dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    print(' ------')

    print(f"{len(some_dict['ubicaciones'])}"+ ' Ubicaciones')
    for i in some_dict['ubicaciones']:
        print(i)

    print(' --------')

    print(f"{len(some_dict['instructores'])}" +' Instrucciones')
    for i in some_dict['instructores']:
        print(i)

printInfo(dojo)

