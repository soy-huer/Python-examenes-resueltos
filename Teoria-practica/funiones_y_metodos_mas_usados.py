# ----------------------------------------------
# TEMA: FUNCIONES MÁS USADAS EN PYTHON
# ----------------------------------------------

# ----------- FUNCIONES/MÉTODOS DE TEXTO (str) -----------

texto = "hola mundo"

print(texto.upper())        # Convierte a MAYÚSCULAS → "HOLA MUNDO"
print(texto.lower())        # Convierte a minúsculas → "hola mundo"
print(texto.capitalize())   # Primera letra en mayúscula → "Hola Mundo"
print(texto.title())        # Capitaliza cada palabra → "Hola Mundo"
print(texto.strip())        # Quita espacios al principio/final
print(texto.replace("mundo", "Python"))  # Reemplaza texto → "hola Python"
print("mundo" in texto)     # Verifica si contiene → True
print(len(texto))           # Longitud del texto → 10
print(texto.count("o"))     # Cuenta cuántas veces aparece "o" = 2

# ----------- FUNCIONES/MÉTODOS DE NÚMEROS -----------

numero = -8.75

print(abs(numero))          # Valor absoluto → 8.75
print(round(numero))        # Redondear → -9
print(pow(2, 3))            # Potencia (2^3) → 8
print(max(3, 7, 2))         # Mayor valor → 7
print(min(3, 7, 2))         # Menor valor → 2
print(float(10))            # Convertir a decimal → 10.0
print(int(5.9))             # Convertir a entero → 5

# ----------- FUNCIONES/MÉTODOS DE LISTAS -----------

frutas = ["manzana", "banana", "pera", "uva"]

print(len(frutas))          # Cantidad de elementos → 3
frutas.append("uva")        # Agrega al final
print(frutas)
frutas.insert(1, "kiwi")    # Inserta en posición 1
print(frutas)
frutas.remove("banana")     # Elimina "banana"
print(frutas)
print(frutas.pop())         # Quita el último y lo muestra
print(frutas)
print(frutas.index("pera")) # Muestra la posición de "pera"
print("manzana" in frutas)  # Verifica si está → True
frutas.sort()               # Ordena alfabéticamente
print(frutas)
frutas.reverse()            # Invierte el orden
print(frutas)

# ----------------------------------------------
# FIN DEL ARCHIVO EDUCATIVO DE FUNCIONES ÚTILES
# ----------------------------------------------
