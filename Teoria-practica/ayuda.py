# 1. Definimos el valor total y el porcentaje que queremos calcular
total = 5000
porcentaje_a_aplicar = 15

resultado = (total * porcentaje_a_aplicar) / 100

print(f"El {porcentaje_a_aplicar}% de {total} es: {resultado}")

total_con_plus = total + resultado
print(f"El total con el recargo es: {total_con_plus}")

#---------------------------------------------------------------------
#simbolos en python
print(100 % 10)  #modulo
print(100 // 7)  #divide y redondea

#descuento de un prodcuto dando cantidad y precio
cantidad = 10
precio = 100

#descuento 
descuento = 100 * 0.15
total = precio - descuento

precio_total = total * cantidad

print("El costo total menos el descuento es:",precio_total)

#Como calcular porcentaje
total = 10000
sucursal_1=2000

porcentaje = (sucursal_1/total)*100

print("El porcentaje que aporto mi sucursal es:", int(porcentaje),"%")

#Diferencia entre Listas, Tuplas y diccionarios

lista = [23,"texto",False,2.6,23,23,23]

tupla = (23,"texto",False,2.6)

diccionario = {1:"uno", 2:"dos", 3:"tres", 5:True, 8:5.6, 9:"uno"}










