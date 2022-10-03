
#objeto lineas
archivo = 'text.txt'
with open(archivo, 'r') as f:
    lines = f.readlines()
#print (lines)
#Cantidad dentro de la lista 
a = len(lines)
print ("La cantidad de lineas que tiene el texto es " f'{a}')

#Bucle for sobre lines
for num, text in enumerate(lines):
    print(f" El numero de linea es {num} y el texto es '{text}' tambien el tipo de dato es {type(text)}")

#Calcular el numero de caracteres 
texto = open('text.txt', 'r')
caracteres = 0
for i in texto:
    caracteres += len(i)
print(f"El total de caracteres por linea es {caracteres}")  

