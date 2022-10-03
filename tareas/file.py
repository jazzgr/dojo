num1 = 42 #declaracion de variable entero
num2 = 2.3 #declaracion de variable float
boolean = True #declaracion de variable booleano
string = 'Hello World' #declaracion de variable cadena
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #declaracion de lista/array con cadenas dentro
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #diccionario
fruit = ('blueberry', 'strawberry', 'banana') #lista
print(type(fruit)) #imprime la funcion lista
print(pizza_toppings[1]) #imprime del array la posicion 1
pizza_toppings.append('Mushrooms') #agrega al arrar mushrooms
print(person['name']) #imprime el diccionario name
person['name'] = 'George' # cambia en el diccionario el nombre por george
person['eye_color'] = 'blue' # cambia en el diccionario por un nuevo valor
print(fruit[2]) #imprime la funcion fruit posicion 2

""" Lo siguiente son condicionales if, else 
despues tenemos bucles for y bucles while"""

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop() #el pop quita el ultimo valor 
pizza_toppings.pop(1) #el pop quita el valor 1

print(person) #imprime la variable person
person.pop('eye_color') #borra de la variable person eye_color
print(person) #imprime la variable person sin el eye_color

"""
Lo siguiente es un bucle for con condicional if
"""
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
"""
Los def son funciones llamadas con y sin parametros (____)

"""
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() #imprime la funcion
print_hello_x_or_ten_times(4) #imprime la funcion con el parametro 4


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)