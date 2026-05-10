#EXAMEN N° 1 : LIBRERÍA - Sistema de Ventas
'''
Contexto: una librería quiere analizar el rendimiento de sus ventas diarias por artículo.
Se registrará cada venta con su artículo, rubro, precio y unidades vendidas para luego generar reportes.
 
1) Registro de Datos:
 Solicitar al usuario la cantidad de ventas a registrar.
 Por cada venta, ingresar:
 Artículo (texto)
 Rubro (1 = Útiles escolares, 2 = Literatura, 3 = Técnica, 4 = Varios)
 Precio unitario (validar número positivo con try-except)
 Unidades vendidas (validar entero positivo con try-except)
 Almacenar los datos en listas paralelas: articulos, rubros, precios, unidades.
 
2) Funcionalidades del Sistema:
l programa debe mostrar un menú con estas opciones:
	1   Mostrar todas las ventas con: artículo, rubro (en texto), precio, unidades y monto de la venta (precio × unidades).
	2.	Mostrar el artículo con mayor monto de venta.
	3.	Mostrar el artículo con menor monto de venta.
	4.	Calcular y mostrar el promedio de monto vendido (sobre todas las ventas).
	5.	Mostrar los artículos cuyo monto vendido supera el promedio.
	6.	Calcular y mostrar el porcentaje de ventas del rubro “Literatura” (código 2).
	7.	Contar cuántas ventas tuvieron unidades ≥ 5.
	8.	Buscar una venta por nombre de artículo y mostrar su rubro, precio, unidades y monto.
	9.	Mostrar el total general vendido (suma de todos los montos).
	10.	Salir del programa.

Requisitos
Implementar funciones con envío de parámetros y retorno de valor para cada punto del menú.
Usar ciclos (for, while) y estructuras de selección (if/elif/else).
Se permite el uso de funciones como sum(), min(), max(), etc. (si querés, podés pedir una variante sin estas funciones).
Validar entradas numéricas con try-except.
Trabajar siempre con listas paralelas.
'''
#Pasos
# Ejercicio 1 - Cargar listas:
# Solicitar los datos al usuario(artículo, rubro, precio, unidades y monto(precio x unidad).
# llenar las listas con esos datos.

# Ejercicio 2 - Menú:
# 1. Mostrar todas las ventas.
# 2. Mostrar artículo con mayor monto.
# 3. Mostrar artículo con menor monto.
# 4. Mostrar Promedio de venta.
# 5. Mostrar montos que superen al promedio.
# 6. Calcular porcentaje de ventas de "Literatura".
# 7. Calcular ventas con unidades mayores o iguales a 5.
# 8. Buscar una venta por el nombre del artículo y mostrar rubro, precio, unidades y monto.
# 9. Mostrar el total general (suma de todos los montos).
# 10. Salir del programa(menu)

#------------------- DESARROLLO EXAMEN N° 1 : LIBRERÍA - Sistema de Ventas -------------------
#Punto 1): Cargar listas
def cargar_listas():
    articulos = []
    rubros = []
    precios = []
    unidades = []
    
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de ventas: ")) #uno
            if cantidad > 0:
                break
            print("La cantidad debe ser mayor a cero.")
        except:
            print("Ingrese un numero valido.")
    
    for i in range(cantidad):
        articulo = input("Ingrese el nombre del artículo: ").lower()
        
        while True:
            try:
                rubro = int(input("Rubro (1-Utiles, 2-Literatura, 3-Tecnica, 4-Varios): "))
                if rubro >= 1 and rubro <= 4:
                    break
                print("Rubro incorrecto.")
            except:
                print("Ingrese un numero.")
    
        while True:
            try:
                precio = float(input("Precio: "))
                if precio > 0:
                    break
                print("El precio debe ser positivo.")
            except:
                print("Ingrese un numero.")

        while True:
            try:
                uni = int(input("Unidades: "))
                if uni > 0:
                    break
                print("Las unidades deben ser positivas.")
            except:
                print("Ingrese un numero.")

        articulos.append(articulo)
        rubros.append(rubro)
        precios.append(precio)
        unidades.append(uni)
                                                  #       0     1   2  3
    return articulos, rubros, precios, unidades   #(["cuaderno"],[],[],[])


#Punto 2): 1. - Mostrar todas las ventas.
def mostrar_ventas(articulos, rubros, precios, unidades):
    if len(articulos) == 0:
        print("No hay ventas cargadas.")
        return
    
    for i in range(len(articulos)):
        print(f"---------------------- Artículo N° {i+1} ----------------------")
        print("Articulo:", articulos[i]) #[0]
        print("Rubro:", rubros[i])
        print("Precio:", precios[i])
        print("Unidad/es:", unidades[i])
        print("Monto:", precios[i] * unidades[i])
        print("-----------------------------------------------------------")
  
  
#Punto 2): 2. - Mostrar artículo con mayor monto.
def mayor_monto(articulos, precios, unidades):
    if len(articulos) == 0:
        print("No hay datos.")
        return
    
    max_monto = precios[0] * unidades[0]
    indice = 0

    for i in range(len(articulos)):
        monto = precios[i] * unidades[i]
        if monto > max_monto:
            max_monto = monto
            indice = i

    print(f"Mayor venta: {articulos[indice]} Monto: {max_monto}.")
    

#Punto 2): 3. - Mostrar artículo con menor monto.
def menor_monto(articulos, precios, unidades):
    if len(articulos) == 0:
        print("No hay datos.")
        return
    
    min_monto = precios[0] * unidades[0] #Empezamos con el primer monto para comparar con los siguientes
    indice = 0

    for i in range(len(articulos)):
        monto = precios[i] * unidades[i]
        if monto < min_monto:
            min_monto = monto
            indice = i

    print(f"Menor venta: {articulos[indice]} Monto: {min_monto}.")



#Punto 2): 4. - Mostrar Promedio de monto vendido (sobre todas las ventas).
#promedio 
'''
suma = 9 + 8 + 10   
cantidad_variables = 3

promedio = suma / cantidad_variables = 9 
'''
def promedio_monto(precios, unidades):
    if len(precios) == 0:
        print("No hay datos.")
        return 0
    
    total = 0
    for i in range(len(precios)):
        total += precios[i] * unidades[i]

    promedio = total / len(precios)
    return promedio 
 

#Punto 2): 5. - Mostrar los artículos cuyo monto vendido supera el promedio.
def sobre_promedio(articulos, precios, unidades, promedio):
    if len(articulos) == 0:
        print("No hay datos.")
        return
    
    for i in range(len(articulos)):
        monto = precios[i] * unidades[i] #300  400
        if monto > promedio:
            print(f"Supera promedio: {articulos[i]} - {monto}$")


#Punto 2): 6. - Calcular porcentaje de ventas de 'Literatura'. 
'''
=======================================================
FÓRMULA MATEMÁTICA DEL PORCENTAJE:
Porcentaje = (Cantidad / Total) * 100
Porcentaje = (20 / 100) * 100 = 20%

- Cantidad: Cantidad de ventas de 'Literatura' (contador)
- Total: Cantidad total de rubros procesados (len)

=======================================================
'''

def porcentaje_literatura(rubros):
    if len(rubros) == 0:
        print("No hay datos.")
        return
    
    contador = 0
    for rubro in rubros:
        #rubro es 2 porque literatura es la opcion 2
        if rubro == 2:  #Rubro (1-Utiles, 2-Literatura, 3-Tecnica, 4-Varios)
            contador += 1

    porcentaje = (contador / len(rubros)) * 100
    
    return porcentaje
    

#Punto 2): 7. - Calcular ventas que tuvieron unidades ≥ 5.
def unidades_5(unidades):
    if len(unidades) == 0:
        print("No hay datos.")
        return
    
    contador = 0
    for i in unidades:
        if i >= 5:
            contador += 1

    return contador


#Punto 2): 8. - Buscar una venta por el nombre del artículo y mostrar datos.
def buscar_articulo(articulos, rubros, precios, unidades):
    if len(articulos) == 0:
        print("No hay artículos en la lista.")
        return
    
    nombre = input("Ingrese articulo a buscar: ").lower()
    encontrado = False

    for i in range(len(articulos)):
        if articulos[i] == nombre:
            print("---------------------- Artículo encontrado ----------------------")
            print("-----------------------------------------------------------------")
            print("Articulo:", articulos[i])
            print("Rubro:", rubros[i])
            print("Precio:", precios[i])
            print("Unidad/es:", unidades[i])
            print("Monto:", precios[i] * unidades[i])
            encontrado = True
            print("-----------------------------------------------------------------")
     
    #El if solo funciona la condicion es verdadera, usamos el not para invertir la condicion.       
    if not encontrado: 
        print("No encontrado.")
  

#Punto 2): 9. - Mostrar el total general vendido (suma de todos los montos).     
def total_general(precios, unidades):
    if len(precios) == 0:
        print("No hay datos.")
        return
    
    total = 0
    for i in range(len(precios)):
        total += precios[i] * unidades[i]

    return total


#Punto 2 - Menú
def principal():
    #Punto 1
    print("\n------------------- LIBRERÍA - Sistema de Ventas -------------------\n")
    print("-------------------- Registrar venta --------------------")
    datos = cargar_listas()  #([articulos],[rubros],[precios],[unidades])
    
    articulos = datos[0]
    rubros = datos[1]
    precios = datos[2]
    unidades = datos[3]
    
    #articulos, rubros, precios, unidades = cargar_listas()
    print("-------------------- Ventas cargadas --------------------")

    #Punto 2
    while True:
        print("\n----------------- LIBRERÍA - Sistema de Ventas Menú -----------------")
        print("1 - Mostrar todas las ventas.")
        print("2 - Mostrar artículo con mayor monto.")
        print("3 - Mostrar artículo con menor monto.")
        print("4 - Mostrar Promedio de monto vendido (sobre todas las ventas).")
        print("5 - Mostrar los artículos cuyo monto vendido supera el promedio.")
        print("6 - Calcular porcentaje de ventas de 'Literatura'.")
        print("7 - Calcular ventas que tuvieron unidades ≥ 5.")
        print("8 - Buscar una venta por el nombre del artículo y mostrar datos.")
        print("9 - Mostrar el total general vendido (suma de todos los montos).")
        print("10 - Salir del programa.")
        print("--------------------------------------------------------------------\n")

        try:
            opcion = int(input("Opcion: "))
        except ValueError:
            print("Ingrese una opcion valida")
            continue

        if opcion == 1:
            mostrar_ventas(articulos, rubros, precios, unidades)
        elif opcion == 2:
            mayor_monto(articulos, precios, unidades)
        elif opcion == 3:
            menor_monto(articulos, precios, unidades)
        elif opcion == 4:
            promedio = promedio_monto(precios, unidades)
            print(f"Promedio: {promedio}.")
        elif opcion == 5:
            prom = promedio_monto(precios, unidades)  
            sobre_promedio(articulos, precios, unidades, prom)
        elif opcion == 6:
            porcentaje = porcentaje_literatura(rubros)
            print(f"Porcentaje Literatura: {porcentaje}%.")
        elif opcion == 7:
            cantidad = unidades_5(unidades)
            print(f"La cantidad de ventas con >=5 unidades es: {cantidad}.")
        elif opcion == 8:
            buscar_articulo(articulos, rubros, precios, unidades)
        elif opcion == 9:
            total = total_general(precios, unidades)
            print(f"El total general es: {total}$.")
        elif opcion == 10:
            print("Saliendo del programa...")
            print("------------------- Fin del programa. -------------------")
            break
        else:
            print("Opcion incorrecta. Intente de nuevo.")

principal()





































