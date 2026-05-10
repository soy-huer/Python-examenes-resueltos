# --------------------------------------------------------
# CONCEPTOS BÁSICOS DE PROGRAMACIÓN
# --------------------------------------------------------

# ¿QUÉ ES UN ALGORITMO? conjunto pasos ordenados y finitos para resolver un problema.
# Es un conjunto de pasos ordenados y finitos que permiten resolver un problema.
# Por ejemplo, una receta de cocina es un algoritmo.

# ¿QUÉ ES UN PROGRAMA?
# Es un conjunto de instrucciones escritas en un lenguaje de programación
# que la computadora puede entender y ejecutar.

# ¿QUÉ ES UN LENGUAJE DE PROGRAMACIÓN?
# Es un idioma formal que se utiliza para escribir programas.
#Es un lenguaje especial que usamos para escribir algoritmos que la computadora puede ejecutar.
# Ejemplos: Python, Java, C++, JavaScript, etc.

# TIPOS DE LENGUAJES DE PROGRAMACIÓN:

# 1. LENGUAJE DE MÁQUINA:
# Es el lenguaje que entiende directamente el procesador (1 y 0 — binario).
# Es muy rápido pero muy difícil de escribir para humanos.

# 2. LENGUAJE DE BAJO NIVEL:
# Se parece un poco más al lenguaje humano, pero sigue siendo cercano al hardware.
# Ejemplo: lenguaje ensamblador (assembly).
# Se usa para controlar directamente componentes como memoria o CPU.

# 3. LENGUAJE DE ALTO NIVEL:
# Es fácil de leer y escribir para las personas.
# Se parece más al lenguaje humano.
# Ejemplos: Python, Java, JavaScript, C#, etc.

# Python es un lenguaje de alto nivel.

# --------------------------------------------------------

# ¿QUÉ ES UNA VARIABLE?
# Es un espacio donde guardamos un dato. Tiene un nombre y un valor.

name = "Romero Anita"    # variable tipo texto 
age = 23          # variable tipo entero
altura = 1.64      # variable tipo decimal
es_estudiante = True  # variable booleana (True/False)

# ¿QUÉ ES UNA CONSTANTE?
# Es un valor que no cambia. En Python, por convención, se escribe en mayúsculas.
PI = 3.14159  

# ¿QUÉ ES UNA ESTRUCTURA DE CONTROL?
# Son instrucciones que permiten tomar decisiones o repetir acciones.

# Ejemplo: Estructura condicional (IF)
edad = 20
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

# Ejemplo: Estructura repetitiva (FOR)
for i in range(3):
    print("Repetición número:", i + 1)
    
# --------------------------------------------------------
# ¿QUÉ ES UNA FUNCIÓN?
# Es un bloque de código que realiza una tarea específica.
def saludar():
    print("Hola, esto es una función.")

saludar()
# --------------------------------------------------------
# ¿QUÉ ES UN ERROR (EXCEPCIÓN)?
# Es un problema que ocurre durante la ejecución del programa.
# Python permite "atrapar" errores para que no se cierre el programa.

try:
    numero = int(input("Ingresa un número: "))
except ValueError:
    print("Eso no es un número válido.")
    
#Formula de promedio y porcentaje

#promedio 
suma = 9 + 8 + 10
cantidad_variables = 3

promedio = suma / cantidad_variables = 9 

#Porcentaje  15% 
#Calcular cual es el cantidad del 20% de una clase de 100

#100000 mil devito descuento ----- 5%    100000 --- 100%   x -------- 5%
#100000 mil creedito impuesto ---- 10%

# --------------------------------------------------------
#REFLA DE TRES SIMPLE APLICADA EN LA PORGRAMACIÓN 
# --------------------------------------------------------
'''
x  -------- 50%
100 ------- 100%               1°  

x -------- 1
3 -------- 100% 

x = (5/100) * 100000    0.05      2°
x = (20/100) * 100000   0.20
x = (10/100) * 100000   0.10
x = (15/100) * 100000   0.15
x = (70/100) * 100000   0.7
x = (50/100) * 10000    0.5

descuento  = 100000 * 0.5        3°  simplicamos la formula  0.7   --> 70%/100% = 0.7
total = 100000 - descuento                 .  .  .           0.2   --> 20%/100% = 0.2

impuesto  = 100000 * 0.5
total = 100000 + impuesto

print("El 50% de 10000 es:", total)
'''

# --------------------------------------------------------
# FIN DEL ARCHIVO EDUCATIVO DE CONCEPTOS BÁSICOS
# --------------------------------------------------------
