#EXAMEN N° 3 : PANADERÍA - Sistema de Ventas
'''
Una panaderia vende productos agrupados en 3 (tres) rubros PANADERIA, MASAS Y FACTURAS, desea 
tener una serie de estadisticas de importe recaudado en cada uno de los 12 meses del año 2026
(para ello se debera cargar 3 listas de 12 elementos cada una de ellas.)
Las salidas que se solicitan son las siguientes:

#No usar sum, max o min, count
1) Total recaudado (un solo total) en el mes de ENERO, MAYO, SEPTIEMBRE Y DICIEMBRE
2) Promedio de recaudacion en ventas en MASAS y FACTURAS
3) Rubro de mayor venta anual.     
4) Mes de MAYOR VENTA en PANADERIA
5) Mes de MENOR VENTA en masas 
6) Promedio de VENTAS en JULIO(todos los rubros)
7) Rubro de MAYOR VENTA en DICIEMBRE

NOTA: utilizar metodos con envio y retorno de valor.
NO UTILIZAR FUNCIONES PARA LOS CALCULOS DE MAYOR, MENOR Y PROMEDIO.
'''
# Ejercicio 1 - Cargar listas:
# Crear 3 listas: panaderia, masas y facturas.
# Cada lista debe tener 12 posiciones (una por cada mes del año).
# Solicitar al usuario los importes de cada mes para cada rubro:
# - validar que sean números positivos
# - guardar cada valor en su lista correspondiente

# Ejercicio 2 - Procesos:
# 1. Mostrar el total recaudado en: ENERO, MAYO, SEPTIEMBRE y DICIEMBRE(sumar los 3 rubros en esos meses).
# 2. Calcular el promedio de recaudación en: MASAS y FACTURAS (todos los meses).
# 3. Mostrar el rubro con mayor venta anual(comparar total de panaderia, masas y facturas).
# 4. Mostrar el mes de mayor venta en PANADERIA.
# 5. Mostrar el mes de menor venta en MASAS.
# 6. Calcular el promedio de ventas en JULIO(sumar los 3 rubros y dividir por 3).
# 7. Mostrar el rubro de mayor venta en DICIEMBRE.


#Punto 1): Cargar listas
#Punto 2): 1. - Total recaudado (un solo total) en el mes de ENERO, MAYO, SEPTIEMBRE Y DICIEMBRE.
#Punto 2): 2. - Promedio de recaudacion en ventas en MASAS y FACTURAS.
#Punto 2): 3. - Rubro de mayor venta anual. 
#Punto 2): 4. - Mes de MAYOR VENTA en PANADERIA.
#Punto 2): 5. - Mes de MENOR VENTA en masas.
#Punto 2): 6. - Promedio de VENTAS en JULIO(todos los rubros).
#Punto 2): 7. - Rubro de MAYOR VENTA en DICIEMBRE.

#------------------- DESARROLLO EXAMEN N° 3 : PANADERÍA - Sistema de Ventas -------------------

#Punto 1): Cargar listas
def cargar_datos():
    panaderia = []
    masas = []
    facturas = []

    meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio",
             "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

    for i in range(12):
        print("\nMes:", meses[i])

        while True:
            try:
                p = float(input("Panaderia: "))
                if p >= 0:
                    break
                print("Valor invalido. Intente de nuevo.")
            except:
                print("Error. Intente de nuevo.")

        while True:
            try:
                m = float(input("Masas: "))
                if m >= 0:
                    break
                print("Valor invalido. Intente de nuevo.")
            except:
                print("Error. Intente de nuevo.")

        while True:
            try:
                f = float(input("Facturas: "))
                if f >= 0:
                    break
                print("Valor invalido. Intente de nuevo.")
            except:
                print("Error. Intente de nuevo.")

        panaderia.append(p)
        masas.append(m)
        facturas.append(f)

    return panaderia, masas, facturas  #([panaderia], [masas], [facturas])


#Punto 2): 1. - Total recaudado (un solo total) en el mes de ENERO, MAYO, SEPTIEMBRE Y DICIEMBRE.
def total_meses_clave(pan, mas, fac):
    total = 0  #pan + mas + fac
    indices = [0, 4, 8, 11]

    for i in indices:
        total += pan[i] + mas[i] + fac[i]

    return total


#Punto 2): 2. - Promedio de recaudacion en ventas en MASAS y FACTURAS.
def promedio_masas_facturas(mas, fac):  #suma de masas y facturas / cantidad
    suma = 0  #100000 300000
    cont = 0

    for i in range(12):
        suma += mas[i]
        cont += 1

    for i in range(12):
        suma += fac[i]
        cont += 1
    
    promedio = suma / cont
    return promedio


#Punto 2): 3. - Rubro de mayor venta anual. 
def rubro_mayor_anual(pan, mas, fac):
    total_pan = 0
    total_mas = 0
    total_fac = 0

    for i in range(12):
        total_pan += pan[i]
        total_mas += mas[i]
        total_fac += fac[i]

    if total_pan >= total_mas and total_pan >= total_fac:
        return "Panaderia"
    elif total_mas >= total_pan and total_mas >= total_fac:
        return "Masas"
    else:
        return "Facturas"
    

#Punto 2): 4. - Mes de MAYOR VENTA en PANADERIA.
def mes_mayor_panaderia(pan):
    mayor = pan[0]   #100 200 600
    indice = 0

    for i in range(12):
        if pan[i] > mayor:
            mayor = pan[i]
            indice = i

    return indice


#Punto 2): 5. - Mes de MENOR VENTA en masas.
def mes_menor_masas(mas):
    menor = mas[0]    #400 300 100
    indice = 0

    for i in range(12):
        if mas[i] < menor:
            menor = mas[i]
            indice = i

    return indice


#Punto 2): 6. - Promedio de VENTAS en JULIO(todos los rubros).
def promedio_julio(pan, mas, fac):
    total = pan[6] + mas[6] + fac[6]  #suma / cantidad
    return total / 3


#Punto 2): 7. - Rubro de MAYOR VENTA en DICIEMBRE.
def mayor_diciembre(pan, mas, fac):
    
    if pan[11] > mas[11] and pan[11] > fac[11]:
        return "Panaderia"
    elif mas[11] > fac[11]:
        return "Masas"
    else:
        return "Facturas"


#Menú
def menu():
    print("\n------------------------- PANADERÍA - Sistema de Ventas Menú -------------------------")
    print("1 - Total recaudado (un solo total) en el mes de ENERO, MAYO, SEPTIEMBRE Y DICIEMBRE.")
    print("2 - Promedio de recaudacion en ventas en MASAS y FACTURAS.")
    print("3 - Rubro de mayor venta anual. ")
    print("4 - Mes de MAYOR VENTA en PANADERIA.")
    print("5 - Mostrar el mes de menor venta en MASAS.")
    print("6 - Promedio de VENTAS en JULIO(todos los rubros).")
    print("7 - Rubro de MAYOR VENTA en DICIEMBRE.")
    print("8 - Salir del programa.")
    print("--------------------------------------------------------------------------------------")


#Punto 2 - Menú
def principal():
    #Punto 1
    print("\n------------------- PANADERÍA - Sistema de Ventas -------------------\n")
    print("--------------------------- Registrar venta ---------------------------")
    pan, mas, fac = cargar_datos() 
    # (pan , mas, fac) = cargar_datos()  #([panaderia], [masas], [facturas])
    print("--------------------------- Ventas cargadas --------------------------")


    meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio",
             "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

    while True:
        menu()

        try:
            op = int(input("Opcion: "))
        except:
            print("Ingreso una opción incorrecta. Intente de nuevo.")
            continue

        if op == 1:
            print("Total:", total_meses_clave(pan, mas, fac))

        elif op == 2:
            print("Promedio:", promedio_masas_facturas(mas, fac))

        elif op == 3:
            print("Rubro mayor:", rubro_mayor_anual(pan, mas, fac))

        elif op == 4:
            pos = mes_mayor_panaderia(pan)
            print("Mes:", meses[pos])

        elif op == 5:
            pos = mes_menor_masas(mas)
            print("Mes:", meses[pos])

        elif op == 6:
            print("Promedio Julio:", promedio_julio(pan, mas, fac))

        elif op == 7:
            print("Rubro en Diciembre:", mayor_diciembre(pan, mas, fac))

        elif op == 8:
            print("Fin del programa.1")
            break

        else:
            print("Opcion invalida")


principal()




























