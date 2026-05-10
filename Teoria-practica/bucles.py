
# ----------------------------------------------
# TEMA: BUCLES EN PYTHON (FOR Y WHILE)
# ----------------------------------------------

# BUCLE FOR = para cada
# Se utiliza para recorrer elementos en una secuencia (lista, cadena, rango, etc.)

#for -> listas, tublas, diccionarios, cadenas, rangos, etc.

# Ejemplo 1: recorrer una lista
frutas = ["manzana", "banana", "pera"]
           
for fruta in frutas:
    print(fruta)
    

# Ejemplo 2: recorrer un rango de números
for i in range(5):
    print("Número:", i)  

# Ejemplo 3: sumar números del 1 al 10
suma = 0       
for i in range(5, 11):
    suma += i
print("Suma total:", suma)

texto = "estudiando python"  
for letra in texto:
    print(letra)
    
# --------------------------------------------------------
# BUCLE WHILE = mientras
# Se ejecuta mientras una condición sea verdadera

# Ejemplo 4: contar hasta 5
contador = 0
while contador < 5:
    print("Contando:", contador)
    contador += 1

# Ejemplo 5: pedir una contraseña hasta que sea correcta
clave_correcta = "python123"
entrada = ""
intentos = 0

while entrada != clave_correcta and intentos < 3:
    entrada = input("Ingrese la contraseña: ")
    intentos += 1

if entrada == clave_correcta:
    print("Acceso permitido")
else:
    print("Acceso bloqueado")

# PALABRAS CLAVE EN BUCLES

# break → termina el bucle antes de que termine normalmente
for i in range(10):
    if i == 5:
        break
    print("Con break:", i)

# continue → salta la iteración actual y pasa a la siguiente
for i in range(5):
    if i == 2:
        continue
    print("Con continue:", i)

# ----------------------------------------------
# FIN DEL ARCHIVO EDUCATIVO DE BUCLES
# ----------------------------------------------



























































