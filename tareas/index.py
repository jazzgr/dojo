def di_hola(nombre):
    print("Hola, " + nombre)

di_hola('Jazz')

def di_hola(nombre):
    return "Hola " + nombre
saludo = di_hola("Michael") # el valor devuelto por la función di_hola se asigna a la variable 'saludo'
print(saludo) # esto dará como resultado 'Hola Michael'

