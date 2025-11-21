print("Ejercicio try except - jueves 20 de nov\n")

print("ejercicio 1: convertir texto a numero\n")

try: 
    edad = int(input("¿cuantos años tienes?"))
    print(f"el proximo año tendras { edad + 1 }")
except valueError:
    print("ERROR: debes escribir un numero, no texto")
    
print("ejercicio try except - jueves 20 de nov\n")

print("ejercicio 2: division entre numeros\n")

try:
    numero1 = int(input("escribe el primer numero: "))
    numero2 = int(input_("escribe el segundo numero: "))
    resultado = numero1 / numero2
    print(f"el resultado de {numero1} + {numero2} = {resultado}")
except ZeroDivisionError: 
    print("ERROR: no puedes dividir entre cero")
except ValueError:
    print("ERROR: debes escribir numeros, no texto ")
    
print("ejercicio 3: acceder a elementos de una lista")
try:
    amigos = ["juan", "maria", "carlos", "sofia"]
    posicion = int(input("¿cual es el numero de amigo que quieres ver? (1-4):"))
    # restamos 1 por que las listas empiezan en 0 
    amigo = amigos[posicion - 1]
    print(f"tu amigo es: {amigo}")
except IndexError:
    print("ERROR: ese numero no existe en la lista ")
except ValueError:
    print("ERROR: debes escribir un numero")
    
    
print("ejercicio 4: busqueda en un diccionario")

try:
    telefonos = {
        "yami": "555-1234",
        "allison": "555-5678"
        "saul": "555-9012"
    }
    nombre = input("¿de quien quieres el telefono?")
    telefono = telefono[nombre]
    print(f"el telefono de {nombre} es: {telefono}")
except KeyError:
    print("ERROR: ese nombre no esta en la agenda")
    
print("ejercicio 5: multiplicar numero por texto")
try:
    numero = int(input("¿cuantas veces quieres ver el mensaje? "))
    mensaje = input("¿cual es el mensaje?")
    print(mensaje * numero)
except ValueError:
    print("ERROR: debes escribir un numero entero")
except TypeError:
    print("ERROR: no se puedeb hacer esa operacion")
    
print("ejercicio 6: validar edad para entrar a una peli")
try;
   edad =int(input("¿cuantos años tienes?"))
if edad < 0:
    print("Error: la edad no puede ser negativa")
elif edad <13:
    print("puedes ver peliculas infantiles (6)")
elif edad <16:
    print("puedes ver peliculas para adolescentes (PG-13)")
elif edad <18:
    print("puedes ver peliculas de 15+ (PG-15)")
else: 
    print("puedes ver cualquier peliucla, incluyendo mayores de 18")
except ValueError:
    print("ERROR:debes escribir tu edad como numero")