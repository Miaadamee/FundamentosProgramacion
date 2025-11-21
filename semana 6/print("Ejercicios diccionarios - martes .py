print("Ejercicios diccionarios - martes \n")
print("\nEjercicio 1\n")
#Escribe tus datos 
usuario = {
    "nombre": "pon tu nombre",
    "edad": 18,
    "ciudad": "Monterrey"
}

print("Diccionario completo:")
print(usuario)
print("\nAcceso a valores individuales:")
print("Nombre:", usuario["nombre"])
print("Edad:", usuario["edad"])
print("ciudad:", usuario["ciudad"])


print("\nEjercicio 2\n")
videojuego = {
    "titulo": "minecraft",
    "plataforma": "PC"
}

print("diccionario original:")
print(videojuego)
# Agregar nuevos datos
videojuego["año"] = 2011
videojuego["genero"] = "sandbox"
videojuego["es_multijugador"] = true 
videojuego["precio"] = "gratis"

print("\ndicionario despues de agregar datos:")
print(videojuego)

print("\nNuevos datos agregados:")
print("año:", videojuego["año"])
print("genero:", videojuego["genero"])
print("precio", videojuego["precio"])

print("\nejercicio 3\n")
#agrega tus datos
perfil = {
    "usuario": " tu nombre",
    "seguidores": 500,
    "publicaciones": 25, 
    "ciudad": "tu ciudad"
}

print("perfil original:")
print(perfil)
print("seguidores antes:", perfil["seguidores"])

# Modificar valores (gana mas seguidores)
perfil["seguidores"] = 1250
perfil["publicaciones"] = 45

print("\nperfil actualizado:")
print(perfil)
print("seguidores ahora:", perfil["seguidores"])
print("publicaciones ahora:", perfil["publicaciones"])

print("\nejercicio 4 - eliminar un par clave-valor\n")
#escribe tus datos
cuenta = {
    "usuario": "pon tu usuario",
    "email": "agrega tu email"
    "telefono": "escribe tu numero",
    "ciudad": "pon tu cd"
}

print("cuenta original (con telefono):")
print(cuenta)
# eliminar el numero de telefono por privacidad 
del cuenta ["telefono"]

print("\ncuenta despues de eliminar telefono:")
print(cuenta)
print("\nvertificacion - ¿existe ¨telefono¨?:", "telefono" in cuenta)

print("\nejercicios 5 - len\n")
#agrega vuestra propia peli 
pelicula = {
    "titulo":"avatar"
    "director": "james cameron"
    "año": 2009,
    "genero": "ciencia ficcion",
    "duracion_minutos": 162,
    "calificacion": 8.0
}

print("pelicula")
print(pelicula)

cantidad = len(pelicula)
print("\n¿cuantos datos tiene el diccionario?:", cantidad)
print("el diccionario tiene", cantidad, "pares clave_valor")

print("\nejercicio 6 - obtener las keys\n")
#agrega vuestra cancion fav
cancion = {
    "titiulo": "deja vu"
    "artista": "olivia rodrigo"
    "album": "GUTS"
    "año": 2023,
    "genero": "pop rock"
    "duracion_segundos": 300
}

print("diccionario en cancion:")
print(cancion)
print("\ntodas las claves del diccionario")
claves = cancion.keys()
print(claves)

print("\nejercicio 7: obtener los values")
calificaciones = {
    "economia": 8.5,
    "derecho de aduanas": 9.0,
    "admin de negocios": 8.0,
    "logistica y cadena de suministro": 7.5,
    "mercadotecnica internacional": 9.5
}

print("diccionario de calificaciones:")
print(calificaciones)
print("\ntodos los valores del diccionario:")
valores = calificaciones.values()
print(valores)

print("\nmostrando valores uno por uno:")
for vlor in valores:
    print("-", valor)
print("\npromedio de calificaciones:", sum(valores) / len(valores))
    