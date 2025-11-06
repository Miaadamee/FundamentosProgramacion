print("\nEjercicio 1\n")
canciones = ["As It Was", "Flowers", "vampire", "cruel summer", "calm down"]

print(" MIA CANCIONES FAVORITAS:")
print(canciones[0])
print(canciones[1])
print(canciones[2])
print(canciones[3])
print(canciones[4])


print("\nEjercicio 2\n")
amigos = []

print("lista inicial:", amigos)

amigos.append("andrea")
print("despues de agregar a andrea:", amigos)

amigos.append("meli")
print("despues de agregar a meli:", amigos)

amigos.append("xime")
print("despues de agregar a xime:", amigos)

print(f"\ntotal de amigos: {len(amigos)}")



print("\nEjercicio 3\n")
calificaciones = [98, 90, 88, 92, 89]

# Mostrar todas las calificaciones 
print(" tus calificaciones:", calificaciones)

# calcular el promedio
suma = sum(calificaciones)
promedio = suma / len(calificaciones)
print(f"promedio: {promedio}")

# Encontrar la mejor y peor calificacion
mejor = max(calificaciones)
peor = min(calificaciones)
print(f"mejor calificacion:{mejor}")
print(f"peor calificacion: {peor}")


print("\nejercicio 4\n")
carrito = []
# Agregar productos
print(" agregando productos al carrito...")
carrito.append("iphone 15")
carrito.append("airpords")
carrito.append("funda")
carrito.append("cargador")

print("carrito actual:", carrito)
print(f"productos en el carrito: {len(carrito)}")

# decidiste que no quieres la funda
print("\nEliminado la funda...")
carrito.remove("funda")

print("carrito final:", carrito)
print(f"total de productos: {len(carrito)}")


print("\nejercicio 5\n")

videojuegos = ["minecraft", "fortnite", "valorent", "roblox", "GTA V"]


print(" MI TOP 5 DE VIDEOJUEGOS:")
print(videojuegos)

# Mostrar el primero y el ultimo
print(f"\nMi favorito (posicion 0): {videojuegos[0]}")
print(f"El de la posicion 5 (ultimo): {videojuegos[-1]})
      
# cambiar mi juego favorito
print("\ncambio de opinion...")
videojuegos[0] = "apex legends"

print("top 5 actualizado:")
print(videojuegos)


print("\nejercicio 6 \n")
series = [" Stranger things", "wednesday", "the last of us"]

print("series para ver:", series)

# Agregar una nueva serie
series.append("one piece")
print("agregaste one piece:", series)

# vertificar si una serie esta en tu lista
if "wednesday" in series:
print("\n si tienes wednesday en tu lista")

if "breaking bad" in series:
print("tienes breaking bad")
else:
print(" no tienes breaking bad en tu lista")

# ya viste la primera serie, la eliminas
print(f"\n¡terminaste de ver {series[0]}")
series.pop(0)
print("series restantes:2, series")