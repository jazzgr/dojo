# print(type(24))
# print(type(3.9))
# print(type(3j))
# int_to_float = float(35)
# float_to_int = int(44.2)
# int_to_complex = complex(35)
# print(int_to_float)
# print(float_to_int)
# print(int_to_complex)
# print(type(int_to_float))
# print(type(float_to_int))
# print(type(int_to_complex))

# import random
# print(random.randint(2,5)) 
# proporciona un número aleatorio entre 2 y 5



# first_name = "Zen"
# last_name = "Coder"
# age = 27
# print("Mi nombre es {} {} y tengo {} años de edad.".format(first_name, last_name, age))
# # salida: Mi nombres es Zen Coder y tengo 27 años de edad.
# print("Mi nombre es {} {} y tengo {} años de edad.".format(age,first_name, last_name))
# salida: Mi nombre es 27 Zen y tengo Coder años de edad.
# for x in 'Hello':
#     print(x)

# mi_lista = ["abc", 123, "xyz"]
# for i in range(0, len(mi_lista)):
#     print(i, mi_lista[i])
# # salida: 0 abc, 1 123, 2 xyz
    
# # O 
    
# for v in mi_lista:
#     print(v)
# salida: abc, 123, xyz
#capitales = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
##
#  otra forma de iterar a través de las claves
#for key in capitales.keys():
#   print(key)
# salida: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
# para iterar a través de los valores
#for val in capitales.values():
#   print(val)
# salida: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
# para iterar a través de las claves y valores
#for key, val in capitales.items():
#   print(key, " = ", val)
# salida: Washington = Olympia, California = Sacramento, Idaho = Boise, etc

# establece los valores predeterminados al declarar los parámetros
# def sé_alegre(name='', repeat=2):
# 	print(f"buenos días {name}\n" * repeat)
# sé_alegre()# salida: buenos días (repetida en dos líneas)
# sé_alegre("tim")# salida: buenos días tim (repetida en dos líneas)
# sé_alegre(name="john")# salida: buenos días john (repetida en dos líneas)
# sé_alegre(repeat=6)# salida: buenos días (repetida en 6 líneas)
# sé_alegre(name="michael", repeat=5)# salida: buenos días michael (repetida en 5 líneas)
# NOTA: el nombre de los argumentos no importa si somos explícitos al enviarlos
#sé_alegre(repeat=3, name="kb")# salida: buenos días kb (repetida en 3 líneas)

def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
