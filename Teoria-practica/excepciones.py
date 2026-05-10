# --------------------------------------------------------
# TEMA: MANEJO DE EXCEPCIONES EN PYTHON
# --------------------------------------------------------

# ¿QUÉ ES UNA EXCEPCIÓN?
# Una excepción es un error que ocurre durante la ejecución del programa.
# Python permite manejar estos errores para evitar que el programa se detenga.

# ESTRUCTURA BÁSICA

# try:
#     bloque de código que puede fallar
#     nombre = int(input(":"))
# except TipoDeError:
#     qué hacer si ocurre ese error
# finally: (opcional)
#     código que se ejecuta siempre, ocurra o no un error

# --------------------------------------------------------
# EJEMPLO 1: División segura

try:
    a = float(input("Ingrese el numerador: "))
    b = float(input("Ingrese el denominador: "))
    resultado = a / b
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
except ValueError:
    print("Error: Debe ingresar un número válido.")

# --------------------------------------------------------
# EJEMPLO 2: Manejo general de excepciones

try:
    numero = int(input("Ingrese un número entero: "))
    print("Número ingresado:", numero)
except Exception as e:
    print("Ocurrió un error:", e)

# --------------------------------------------------------
# EJEMPLO 3: Uso de finally

try:
    archivo = open("archivo_inexistente.txt", "r")
except FileNotFoundError:
    print("Error: El archivo no existe.")
finally:
    print("Esta línea se ejecuta siempre (con o sin error).")

# --------------------------------------------------------
# EJEMPLO 4: Lanzar excepciones manualmente

edad = -5
if edad < 0:
    raise ValueError("La edad no puede ser negativa.")

# --------------------------------------------------------
# FIN DEL ARCHIVO EDUCATIVO DE EXCEPCIONES
# --------------------------------------------------------
