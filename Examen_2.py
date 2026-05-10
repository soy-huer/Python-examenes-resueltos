#EXAMEN N° 2 : CLUB de básquet
'''
Club de básquet - reclutando jugadores femeninos y masculinos
1) a)int(input) cantidad jugadores    20
   b)nombre, sexo, edad y la altura(validar que sea positivo edad y altura.
   c)1)nombres 2)sexo 3)edad 4)la altura
   
2) 1)Mostrar todos los datos de los jugadores
   2)Mostrar nombre y edad de jugador masculino mas alto
   3)Promedio altura femenino 
   4) 1.67 > mostrar las jugadoras que sean mas altas a ese promedio
   5) 1.67 < mostrar las jugadoras mas bajas que el promedio
   6) jugadores masculinos mas altos que 2 metros
   7) buscar en lista nombres un jugador por su nombre y mostrar sus datos
   8) promedio de edad para ambos sexos
   9) Cantidad de jugadores > 25 años
   10) Salir del programa
'''
#Pasos
# Ejercicio 1 - Cargar listas:
# Solicitar la cantidad de jugadores.
# Por cada jugador pedir: nombre, sexo (m/f), edad (validar positivo) y altura (validar positivo).
# Guardar los datos en listas paralelas: nombres, sexos, edades, alturas.

# Ejercicio 2 - Menú:
# 1. Mostrar todos los jugadores (nombre, sexo, edad, altura).
# 2. Mostrar nombre y edad del jugador masculino más alto.
# 3. Calcular y mostrar el promedio de altura femenina.
# 4. Mostrar jugadoras con altura mayor al promedio.
# 5. Mostrar jugadoras con altura menor al promedio.
# 6. Mostrar jugadores masculinos con altura mayor a 2 metros.
# 7. Buscar un jugador por nombre y mostrar todos sus datos.
# 8. Calcular y mostrar el promedio de edad (todos los jugadores).
# 9. Contar cuántos jugadores tienen más de 25 años.
# 10. Salir del programa.

#------------------- DESARROLLO EXAMEN N° 2 : CLUB de básquet -------------------

#Punto 1): Cargar listas
def cargar_jugadores():
    nombres = []
    sexos = []
    edades = []
    alturas = []

    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de jugadores: "))
            if cantidad > 0:
                break
            print("La cantidad debe ser mayor a 0.")
        except ValueError:
            print("Ingrese un numero valido.")

    for i in range(cantidad):
        print(f"\n-------------------- Jugador/a {i+1} --------------------")

        nombre = input("Ingrese el nombre: ").lower()

        while True:
            sexo = input("Ingrese el sexo del jugador/a (m/f): ").lower()
            if sexo == "m" or sexo == "f":
                break
            print("Solo se permite ingresar 'm' o 'f'. Intente de nuevo.")

        while True:
            try:
                edad = int(input("Ingrese la edad del jugador/a: "))
                if edad > 0:
                    break
                print("Ingrese una edad valida. Intente de nuevo")
            except ValueError:
                print("Ingrese una edad valida(solo numeros). Intente de nuevo.")

        while True:
            try:
                altura = float(input("Ingrese la altura del jugador/a (ej: 1.75): "))
                if altura > 0:
                    break
                print("Altura invalida. Intente de nuevo.")
            except ValueError:
                print("Debe ingresar un numero. Intente de nuevo.")

        nombres.append(nombre)
        sexos.append(sexo)
        edades.append(edad)
        alturas.append(altura)

    return nombres, sexos, edades, alturas  #([nombres], [sexos], [edades], [alturas]) es una tupla con las 4 listas paralelas


#Punto 2): 1. Mostrar todos los jugadores (nombre, sexo, edad, altura).
def mostrar_todos(nombres, sexos, edades, alturas):
    if len(nombres) == 0:
        print("No hay jugadores registrados.")
        print("No hay datos que mostrar.")
        return

    for i in range(len(nombres)):
        print(f"-------------------- Jugador/a N° {i+1} --------------------")
        print("Nombre: ", nombres[i])
        print("Sexo: ", sexos[i])
        print("Edad: ", edades[i])
        print("Altura: ", alturas[i])
        print("-------------------------------------------------------------")  


#Punto 2): 2. Mostrar nombre y edad del jugador masculino más alto.
def masculino_mas_alto(nombres, sexos, edades, alturas):
    if len(nombres) == 0:
        print("No hay jugadores registrados.")
        print("No hay datos que mostrar.")
        return
    
    max_altura = -1  #comparar con los demas jugadores
    pos = -1          #1.75 1.9 2.3
    
    for i in range(len(nombres)):
        if sexos[i] == "m" and alturas[i] > max_altura:
            max_altura = alturas[i]
            pos = i

    if pos != -1:
        print(f"Masculino más alto: {nombres[pos]} Edad: {edades[pos]}.")
    else:
        print("No hay jugadores masculinos.")


#Punto 2): 3. Calcular y mostrar el promedio de altura femenina.
def promedio_altura_femenino(sexos, alturas):
    if len(sexos) == 0:
        print("No hay jugadoras registradas.")
        print("No hay datos que mostrar.")
        return
    
    suma = 0        #suma/cantidad
    contador = 0

    for i in range(len(sexos)):
        if sexos[i] == "f":
            suma += alturas[i]
            contador += 1

    promedio = suma / contador
    return promedio


#Punto 2): 4. Mostrar jugadoras con altura mayor al promedio.
def femeninas_mayores_prom(nombres, sexos, alturas, promedio):
    if len(nombres) == 0:
        print("No hay jugadoras registradas.")
        print("No hay datos que mostrar.")
        return
    
    #1.8 1.9
    for i in range(len(nombres)):
        if sexos[i] == "f" and alturas[i] > promedio:
            print("Jugadora con altura mayor al promedio: ", nombres[i])


#Punto 2): 5. Mostrar jugadoras con altura menor al promedio.
def femeninas_menores_prom(nombres, sexos, alturas, prom):
    if len(nombres) == 0:
        print("No hay jugadoras registradas.")
        print("No hay datos que mostrar.")
        return
    
    #1.6  1.5
    for i in range(len(nombres)):
        if sexos[i] == "f" and alturas[i] < prom:
            print("Jugadora con altura menor al promedio: ", nombres[i])


#Punto 2): 6. Mostrar jugadores masculinos con altura mayor a 2 metros.
def masculinos_mayores_2m(nombres, sexos, alturas):
    if len(nombres) == 0:
        print("No hay jugadores registrados.")
        print("No hay datos que mostrar.")
        return
    
    for i in range(len(nombres)):
        if sexos[i] == "m" and alturas[i] > 2:
            print("Jugador con altura mayor a 2m: ", nombres[i])


#Punto 2): 7. Buscar un jugador por nombre y mostrar todos sus datos.
def buscar_jugador(nombres, sexos, edades, alturas):
    if len(nombres) == 0:
        print("No hay jugadores registradas/os.")
        print("No hay datos que mostrar.")
        return
    
    nombre = input("Nombre del jugador/a a buscar: ").lower()

    for i in range(len(nombres)):
        if nombres[i] == nombre:
            print("-------------------- Jugador/a encontrado/a --------------------")
            print(f"Nombre: {nombres[i]}, Sexo: {sexos[i]}, Edad: {edades[i]}, Altura: {alturas[i]}.")
            return

    print("Jugador/a no encontrado/a.")


#Punto 2): 8. Calcular y mostrar el promedio de edad (todos los jugadores).
def promedio_edad(edades):
    if len(edades) == 0:
        print("No hay jugadores registradas/os.")
        print("No hay datos que mostrar.")
        return

    # Inicializamos un acumulador en cero
    total_suma = 0
    
    # Recorremos la lista sumando cada edad al total
    for edad in edades:
        total_suma += edad  # Usamos el operador += que vimos antes 

    # La fórmula de promedio: Suma total dividida la cantidad de elementos
    promedio = total_suma / len(edades)   
    
    return promedio

#Punto 2): 9. Contar cuántos jugadores tienen más de 25 años.
def mayores_25(edades):
    if len(edades) == 0:
        print("No hay jugadores registradas/os.")
        print("No hay datos que mostrar.")
        return

    contador = 0     
    for i in edades:
        if i > 25:
            contador += 1

    return contador


#Punto 2 - Menú
def principal():
   #Punto 1
    print("\n------------------- CLUB de Básquet - Sistema de Registro -------------------\n")
    print("-------------------- Registrar jugadores --------------------")
    nombres, sexos, edades, alturas = cargar_jugadores()
    #(nombres, sexos, edades, alturas) = cargar_jugadores()
    #([nombres], [sexos], [edades], [alturas])
    
    print("------------------- Jugadores registrados -------------------")
   
   #Punto 2
    while True:
        print("\n----------------- CLUB de Básquet - Sistema de Registro -----------------")
        print("1 - Mostrar todos los jugadores (nombre, sexo, edad, altura).")
        print("2 - Mostrar nombre y edad del jugador masculino más alto.")
        print("3 - Calcular y mostrar el promedio de altura femenina.")
        print("4 - Mostrar jugadoras con altura mayor al promedio.")
        print("5 - Mostrar jugadoras con altura menor al promedio.")
        print("6 - Mostrar jugadores masculinos con altura mayor a 2 metros.")
        print("7 - Buscar un jugador por nombre y mostrar todos sus datos.")
        print("8 - Calcular y mostrar el promedio de edad (todos los jugadores).")
        print("9 - Contar cuántos jugadores tienen más de 25 años.")
        print("10 - Salir del programa.")
        print("-------------------------------------------------------------------------")
        
        try:
            op = int(input("Ingrese una opcion: "))
        except ValueError:
            print("Error. Intente de nuevo.")
            continue

        if op == 1:
            mostrar_todos(nombres, sexos, edades, alturas)

        elif op == 2:
            masculino_mas_alto(nombres, sexos, edades, alturas)

        elif op == 3:
            promedio = promedio_altura_femenino(sexos, alturas)
            print("Promedio altura femenino: ", promedio)

        elif op == 4:
            promedio = promedio_altura_femenino(sexos, alturas)
            femeninas_mayores_prom(nombres, sexos, alturas, promedio)

        elif op == 5:
            promedio = promedio_altura_femenino(sexos, alturas)
            femeninas_menores_prom(nombres, sexos, alturas, promedio)

        elif op == 6:
            masculinos_mayores_2m(nombres, sexos, alturas)

        elif op == 7:
            buscar_jugador(nombres, sexos, edades, alturas)

        elif op == 8:
            promedio = promedio_edad(edades)
            print("El promedio de edad de todos los jugadores es: ", promedio)
        elif op == 9:
            cantidad = mayores_25(edades)
            print("La cantidad de jugadores mayores a 25: ", cantidad)

        elif op == 10:
            print("Saliendo del programa...")
            print("------------------- Fin del programa. -------------------")
            break

        else:
            print("Opcion invalida. Intente de nuevo.")


principal()































































































