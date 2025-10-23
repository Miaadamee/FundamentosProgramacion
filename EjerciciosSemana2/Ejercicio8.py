
#Ejercicio 8 
print("Ejjercicio 8. operadores logicos")
# Imaginemos que queremos entrar un juego online
tengo_internet = True # Si tengo interne
tengo_cuenta = True # si tengo cuenta 

# AND (Y): LAS DOS condiciones deben ser verdaderas
puedo_jugar = tengo_internet and tengo_cuenta
print("¿puedo jugar? (ambas true):", puedo_jugar)

# Probemos cuando falta algo 
tengo_internet2 = True 
tengo_cuenta2 = False #Python distingue entre mayusculas y minusculas 
puedo_jugar2 = tengo_internet2 and tengo_cuenta2
print("¿puedo jugar? (una es false):", puedo_jugar2)

# OR (o) Al menos UNA condicionm debe ser verdadera 
tengo_celular = True 
tengo_tablet = False 
tengo_dispositivo = tengo_celular or tengo_tablet
print("¿puedo salir? (NOT False = True):", tengo_dispositivo)
