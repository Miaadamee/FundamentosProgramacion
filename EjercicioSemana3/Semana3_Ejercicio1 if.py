

#Ejercicio #1: control de acceso a videojuego
print("Ejercicio 1\n")

edad = int(16)

if edad >16:
   print(" puedes jugar\n")
else:
    print("no puedes jugar\n")
    
    
#Ejercicio #2: calculadora de promedio escolar 
print("Ejercicio 2\n")

calificacion = int(input("Ingresa tu calificacion (0-100):"))

if calificacion >= 90 and calificacion <= 100:
    print("Excelente")
elif calificacion >= 70 and calificacion < 90:
    print("Aprobado")
elif calificacion >= 0 and calificacion < 70:
    print("Ay!, no aprobado")
else:
    print(" Calificacion invalida")
    

#Ejercicio 3
print("otra forma de hacer")
    
edad = int(input("¿cual es tub edad? "))
if edad < 13: 
    print("Te recomendamos peliculas infantiles")
    
elif edad >=13 and edad <= 17:
    genero = input("¿cual es tu genero favorito? (accion, comedia, terror): ").lower()
    
    if genero == "accion": 
        print("te recomendamos: spider_man (PG-13)")
    elif genero == "comedia":
        print("Te recomendamos: Sherk (PG-13)")
    elif genero == "terror":
        print("te recomendamos: Scary stories (PG-13)")
        
    elif edad >=18:
        genero= input("¿cual es tu genero favorito? (accion,comedia,terror):").lower()
        
        if genero == "accion":
            print("te recomendamos: john wick")
        elif genero == "comedia":
            print("te recomendamos: superbad")
        elif genero == "terror":
           print("te recomendamos: el conjuro")
           
# ya funcionan los tres problemas, puedes entregarlos
# solo faltaban : y estaba mal acomodado, pero todo excelente, muy bien trabajo