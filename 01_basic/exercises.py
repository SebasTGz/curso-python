###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

# print("\nEjercicio 1: Imprimir mensajes")
# print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
# print("Mi nombre es Sebastian")
# print("de la ciudad de Ibagué.")

# print("--------------")

# print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
# print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
# a = 15
# b = 3.14159
# c = "Hola mundo"
# d = True
# e = None

# ## Completa aquí
# print("El tipo 'a' es", type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

# print("--------------")

# print("\nEjercicio 3: Casting de tipos")
# print("Convierte la cadena \"12345\" a un entero y luego a un float.")
# print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
# print("Cadena a entero:" , type(int("12345")))
# print("Cadena a float:", type(float("12345")))
# print("El resultado en entero sería:", int(3.99))    
#Al convertir un float a un entero, Python elimina la parte decimal

# print("--------------")

# print("\nEjercicio 4: Variables")
# print("Crea variables para tu nombre, edad y altura.")
# print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí
# nombre="Sebastián G"
# edad= 23
# altura= 1.70

# print(f'Hola! Me llamo {nombre} tengo {edad} años, y mido {altura:.2f} metros')
#Formateamos la altura en un formato f para que muestre 2 decimales en este caso, osea 2 posiciones.

#print("--------------")

# print("\nEjercicio 5: Números")
# print("1. Crea una variable con el número PI (sin asignar una variable)")
# print("2. Redondea el número con round()")
# print("3. Haz la división entera entre el número que te salió y el número 2")
# print("4. El resultado debería ser 1")

### Completa aquí
# print(f'\nLa división daría: {round(3.1416)//2}')
'''
division normal 7/2 = 3.5
division entera 7//2 = 3 , descarta los decimales
'''
# monto = 2100000
# tiempo = 40
# formula = monto * (1+0.10) ** tiempo
# fee = monto*tiempo*0.012
# gan_final = formula - fee

# print(f'Monto Inicial: ${monto:,} pesos.')
# print(f'Total I. Compuesto generado: ${round(gan_final+fee,2):,}')
# print(f'Fee Intereses: $ -{round(fee,2):,}')
# print(f'Capital Final a un plazo de {tiempo} años: $ {round(gan_final,2):,} pesos')