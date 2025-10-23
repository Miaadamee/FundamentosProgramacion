
 #Ejercicio 10.
print("Ejercicio 10. operadores de identidad\n")
 
 #Programa que compra objetos
 
print("=== ¿SON LA MISMA COSA?===")
 # creamos dos listas que se ven iguales
lista1= ["manzana", "pera"] #Faltaba una coma, pero ya la puse, era todo el error, ya funciona
lista2 = ["manzana", "pera"]
lista3 = lista1 #lista3 es la MISMA que lista1

# IS (es): Pregunta ¿son el mismo objeto en la memoria?
print("¿lista1 es lista2? (is):", lista1 is lista2) # False (diferentes objetos)
print("¿lista1 es lista3? (is):", lista1 is lista3) # True (mismo objeto)

# IS NOT (NO ES): Pregunta ¿NO son el mismo objeto?
print("¿lista1 NO es lista2? (is not):", lista1 is not lista2) #True 

#Sube la carpeta de los ejercicios a GitHub
#El enlace o liga de GitHub es lo que vas a entregar de tarea
#Muestrame donde tienes los archivos de codigo python