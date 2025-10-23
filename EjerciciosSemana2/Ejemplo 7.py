# Ejemplo 7. operadores de comparacion 
print("Ejercicio 7. operadores de comparacion")

print("¿He aprobado o no la materia?")
# MAYOR O IGUAL (>=): La calificacion minima para pasar es 70 
calificacion = 70 
resultado5 = calificacion >= 70 #faltaba esta linea
print("¿Aprobe?:" , resultado5)

# Mayor (>): La calificacion minima para pasar es 70 
resultado6 = calificacion > 70
print("¿Aprobe?:", resultado6)


# vamos a comprar estos dos numeros 
mi_edad = 18 
edad_minima = 18 
#IGUAL A (==): pregunta: ¡Loa numeros son iguales?
resultado1 = mi_edad == 15
print("\n¿Soy mayor de edad? (==):", resultado1)

# DIFERENTE DE (!=): pregunta: ¿Los numeros son diferentes?
resultado22 = mi_edad != 20
print(resultado22) #A python no le gusto el mensaje por eso lo quite y deje solo la variable


# MENOR QUE (<): Pregunta: ¿El primer numero es menor?
resultado3 = mi_edad < 18 
print("¿Mi edad es menor que 18? (<):", resultado3)

# MENOR O IGUAL (<=): Pregunta: ¿Es menor o igual?
resultado4 = mi_edad <= 10
print("¿Mi edad es menor o igual a 10? (<=):", resultado4)
