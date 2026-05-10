
# ----------------------------------------------
# TEMA: FUNCIONES Y PROCEDIMIENTOS EN PYTHON
# ----------------------------------------------

# ¿QUÉ ES UNA FUNCIÓN?
# Una función es un bloque de código que realiza una tarea específica.
# Puede recibir parámetros y puede retornar un resultado (o no).

# ESTRUCTURA BÁSICA:
# def nombre_funcion(parámetros):
#     instrucciones
#     return resultado (opcional)

# ----------------------------------------------
# FUNCIÓN QUE NO RECIBE PARÁMETROS NI RETORNA VALOR
def saludar():
    print("Hola, esto es una función sin parámetros ni retorno.")

saludar()  # Llamamos a la funcion por su nombre

# ----------------------------------------------
# FUNCIÓN QUE RECIBE PARÁMETROS PERO NO RETORNA
def saludar_usuario(nombre):
    print(f"Hola, {nombre}!")

saludar_usuario("Anita")

# ----------------------------------------------
# FUNCIÓN QUE NO RECIBE PARÁMETROS PERO RETORNA VALOR
def obtener_pi():
    return 3.14159

pi = obtener_pi()

print("El valor de pi es:", pi)

# ----------------------------------------------
# FUNCIÓN QUE RECIBE PARÁMETROS Y RETORNA VALOR
def sumar(a, b):
    suma = a + b
    return suma

resultado = sumar(5, 3)
print("Resultado de la suma:", resultado)

# ---------------------------------------------------------------------------------------------------------------------------------
# USO DE FUNCIONES COMO PROCEDIMIENTOS
# Si una función no tiene return, actúa como un procedimiento.
# Solo realiza acciones (mostrar, guardar, etc.) pero no devuelve valor.

def mostrar_mensaje(msg):
    print("Mensaje:", msg)

mostrar_mensaje("Este es un procedimiento.")

# ----------------------------------------------
# FUNCIONES CON VALORES POR DEFECTO
def saludar_persona(nombre="usuario"):
    print(f"Bienvenido/a, {nombre}!")

saludar_persona()           # Usa valor por defecto
saludar_persona("Romero")   # Usa valor ingresado

# ----------------------------------------------
# FIN DEL ARCHIVO EDUCATIVO DE FUNCIONES
# ----------------------------------------------


#Funcion
def cheff(Tapas, jamon, queso, temperatura):
    horno = 65
    tarta = Tapas + jamon + queso
    tartaLista = tarta + horno
    
    return tartaLista

Tapas = "Tapas"
jamon = "jamon"
queso = "queso"
temperatura = 80

cheff(Tapas,jamon,queso,temperatura)


#procedimiento
def secretaria():
    print("Hoy se atiende a partir de las 8 a.m hasta las 9 p.m")


secretaria()