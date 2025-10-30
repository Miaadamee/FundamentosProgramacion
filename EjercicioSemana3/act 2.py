# Programa para cobrar entradas al museo de antropologia e Historia

print("¡Bienvenido al museo de antropologia e Historia!")

#Precios 
precio_menor = 30 #Menores de 18 años 
precio_mayor = 45 #Mayores de 18 años

#Pedir numero de visitantes 
visitantes = int(input("Ingrese el lnumero de visitantes que pagaran boleto:"))
total = 0
contador = 0 
print("\nvisitante",contador + 1 ) 

edad = int(input("Ingrese la edad del visitante:"))
edad < 3
print("No paga boleto (menor de 3 años)")
contador += 1 
# pasa al siguiente visitante
edad < 18 
precio = precio_menor 
precio = precio_mayor 
print("Tipos de visitante:")
print("1. adulto mayor")
print("2. profesor")
print("3. estudiante")
print("4. ninguno")
tipo = input("Ingrese el numero correspondiente:")
tipo == "1" and edad > 60:
descuento = 0.12
tipo == "2": 
descuento = 0.10
tipo == "3":
descuento = 0

pago= precio - (precio * descuento)
print("Precio base:", precio)
print("Descuento aplicado:", descuento*100,"%")
print("Total a pagar por este visitante:", pago)

total += pago 

# Preguntar si quiere detener el proceso 
salir = input("¿Desea detener el cobro de visitantes? (s/n):") 
salir == "s"
print("Proceso detenido por el usuario.")
break 

contador +=1 #Aumenta el contador para pasar al siguiente visitante

print("\nE1 total a pagar por todas las entradas es:", total)
print("¡Gracias por visitar el museo!")

    