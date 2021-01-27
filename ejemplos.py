# INPUT /// raw_input

username = input("Enter username:")
print("Username is: " + username)


horas = float(input("Introduce tus horas de trabajo: "))
coste = float(input("Introduce lo que cobras por hora: "))
paga = round(horas * coste, 3)
print("Tu paga es " + str(paga))


#CONDICIONALES 

edad = int(input("¿Cuál es tu edad? "))
if edad < 18: 
    print ("Eres menor de edad.")
else:
    print("Eres mayor de edad.")


edad = int(input("Introduce tu edad: "))
# Decisión de la categoria en función de la edad
if edad < 13:
    cat = "Infantil"
elif edad <= 18:
    cat = "Junior"
elif edad <= 40:
    cat = "Senior"
else:
    cat = "Veterano"
# Mostrar 
print("La categoría que corresponde es: ", cat)

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

thistuple = ("apple", "banana", "cherry")
#len: devuelve la longitud de un objeto
print(len(thistuple))


#CICLOS 

word = input("Introduce una palabra: ")
for i in range(10):
    print(word)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


for x in "banana":
  print(x) 

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


n = int(input("Introduce un número entero positivo: "))
for i in range(1, n+1, 2):
    print(i, end=", ")


animales = ['gato', 'perro', 'conejo']
for animal in animales:
    print(animal)

# Y ahora si los queremos numerar:

animales = ['gato', 'perro', 'conejo']
#Enumera los elementos de una lista u objeto iterable
for idx, animal in enumerate(animales):
    print('#%d: %s' % (idx + 1, animal))

# Trabajando con listas de números

nums = [0, 1, 2, 3, 4]
cuadrado = []
for x in nums:
    #Append: agregar elementos
    cuadrado.append(x ** 2)
print(cuadrado)

# Y podemos colocar operaciones y condiciones al operar una lista

nums = [0, 1, 2, 3, 4]
cuadrados_p = [x ** 2 for x in nums if x % 2 == 0]
print(cuadrados_p)

#WHILE
i = 1
while i < 6:
  print(i)
  i += 1

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#FUNCIONES

# En Python, la definición de funciones se realiza mediante la instrucción def
# más un nombre de función descriptivo seguido de paréntesis de apertura y
# cierre. La definición de la función finaliza con dos puntos (:) y el algoritmo que
# la compone, irá identado con 4 espacios:

# def mi_funcion():
# aquí el código

# Una función, no es ejecutada hasta que no sea invocada. Para invocar una
# función, simplemente se la llama por su nombre.
# La función podrá ser llamada con menos argumentos de los que espera:

def saludar(nombre, mensaje='Hola'):
  print (mensaje, nombre)
  saludar('Clase')
  saludar(mensaje="Buen día", nombre="Juan")


def square(sample):
    """Función que calcula los cuadrados de una lista de números.
    Parámetros
    sample: Es una lista de números
    Devuelve una lista con los cuadrados de los números de la lista sample.
    """
    list = []
    for i in sample:
        list.append(i**2)
    return list

print(square([1, 2, 3, 4, 5]))
print(square([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))


def to_decimal(n):
    n = list(n)
    n.reverse()
    decimal = 0
    for i in range(len(n)):
        decimal += int(n[i]) * 2 ** i
    return decimal

#print(to_d('10110'))

def count_words(text):
    text = text.split()
    words = {}
    for i in text:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    return words

text = 'Si me dieran a elegir, yo elegiría esta salud de saber que estamos muy enfermos, esta dicha de andar tan infelices.'

print(count_words(text))

text.count('yo')
text.count('esta')
text.count('es')

#NumPy (Numerical Python)

# Es una de las bibliotecas más populares de Python, es usado para realizar operaciones 
# con vectores o matrices de una manera eficiente. Contiene funciones de Álgebra Lineal, 
# transformadas de Fourier, generación de números aleatorios e integración con Fortran, C y C++. 

#Fuente: http://www.numpy.org/

import numpy as np

a = np.zeros((2,2))   
print(a)              

b = np.ones((1,2))    
print(b)              

c = np.full((2,2), 7) 
print(c)              

d = np.eye(2)         
print(d)              

e = np.random.random((2,2))
print(e)
#Otro ejemplo
import numpy as np

x = np.array([[1,2],[3,4]])

print(np.sum(x))
print(np.sum(x, axis=0))

"""
Ejemplo para la creación de gráficas 3D

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.viridis)

plt.show()

def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while 1:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'): return 1
        if ok in ('n', 'no'): return 0
        retries = retries - 1
        if retries < 0: print("Bloqueado") 
        print complaint

ask_ok('Really?')


/************** BIBLIOTECAS

import calendar

print(calendar.day_name[0])

calendar.weekday(1984,1,23)

calendar.weekheader(2)

calendar.calendar(2020)


pato.calendar(2020)

import calendar as pato
"""