# --------------------------------------------------------
# TEMA: TIPOS DE DATOS Y OPERADORES EN PYTHON
# --------------------------------------------------------

# TIPOS DE DATOS EN PYTHON

# 1. Números enteros (int) 
edad = 25           # Un número entero

# 2. Números decimales (float)
altura = 1.75       # Un número con decimales

# 3. Cadenas de texto (str)
nombre = "Luis "    # Texto entre comillas

# 4. Booleanos (bool)
es_estudiante = True   # Solo puede ser True o False

# 5. Listas (list)
frutas = ["manzana", "banana", "pera"] #mutables se pueden cambiar los datos
precioFrutas = [10,20,5]               #Lista son mas lentas y pesadas, sueles usarse von bucles porque son dinamicas

precioFrutas[0]

# 6. Tuplas (tuple)
punto = (10, 20) #inmutables los datos no se pueden cambiar puedo imprimir los datos pero cambiarlos
                 #Son mas livianas y rapidas porque solo muestran datos

# 7. Diccionarios (dict)
persona = {"nombre": "Anita", "edad": 25, "estudiante":True}
producto ={"producto":"manzana", "precio":20, "iva":12}

# 8. Conjuntos (set)
numeros = {1, 2, 3} 
# --------------------------------------------------------
# OPERADORES EN PYTHON
# --------------------------------------------------------

# OPERADORES ARITMÉTICOS
a = 10
b = 3

print(a + b)    # Suma: 13
print(a - b)    # Resta: 7
print(a * b)    # Multiplicación: 30
print(a / b)    # División: 3.333...
print(a // b)   # División entera: 3
print(a % b)    # Módulo (resto): 1
print(a ** b)   # Potencia: 1000

# OPERADORES DE COMPARACIÓN o  relacionales
print(a == b)   # Igualdad: False
print(a != b)   # Distinto: True
print(a > b)    # Mayor que: True
print(a < b)    # Menor que: False
print(a >= b)   # Mayor o igual que: True
print(a <= b)   # Menor o igual que: False

# OPERADORES LÓGICOS solo comparan valores verdadero o falso 
x = True
y = False

print(x and y)  # AND lógico: False
print(x or y)   # OR lógico: True
print(not x)    # NOT lógico: False

True = verdadero
False = falso

#Operador And (y)  solo verdadero cuando ambas expreciones son verdaderas
V  and  V = V   
V  and  F = F
F  and  V = F
F  and  F = F

#Operador OR (ó)  Que devuelve verdadero si aunque sea un aexpresion se verdadera
V  or V  or V= V
V  or F = V
F  or V = V
F  or F  = F


# OPERADORES DE ASIGNACIÓN
contador = 5
contador += 1   # contador = contador + 1 → ahora vale 6

# OPERADORES DE PERTENENCIA
print("banana" in frutas)    # True
print("uva" not in frutas)   # True
# --------------------------------------------------------
# FIN DEL ARCHIVO EDUCATIVO
# --------------------------------------------------------











































