#Actividad 1:

#Define variables para almacenar el nombre, edad y profesión del usuario.

#Solicita estos datos por teclado utilizando input().

#Imprime en pantalla un mensaje personalizado incluyendo todos estos datos.


#NOMBRE

nombre = "Luis"
edad = 46
Profesión = "Tester"

#Entrada y Salida de datos

nombre = input("ingresa tu nombre :")
edad = int(input("ingresa tu edad :"))
profesión = input("ingresa tu profesión :")

print(f"bienvenido {nombre}, aqui podrás mejorar tu profesión de: {profesión}") 


#Actividad 2:
#Escribe un pequeño script que utilice un bucle para mostrar los primeros 10 números pares.
#Usa condicionales para validar y mostrar sólo los números pares.


for i in range(2,21,2):
    print(i)

#otra forma de ver los primeros 10 numeros pares sin sabe donde va a cortar puede ser esta:

for i in range(2,50,2):
    if i == 10:
        break


# RANGE #

#range(stop) 10
#range(start, stop) 2 - 11
#range(start, stop, step) 2 - 11 -- 2#
#BUCLES#



# 3. Usando f-strings (cadenas formateadas) para incluir variables en el texto
#print(f"La persona {nombre} tiene {edad} años y vive en {ciudad}.")
# Salida: La persona Juan tiene 30 años y vive en Buenos Aires.

#año_de_nacimiento = input("ingresa tu año de nacimiento :")
#convertido_a_numero = int(año_de_nacimiento)
#print(año_de_nacimiento)#
#o de esta forma

#año_de_nacimiento = int(input("ingresa tu año de nacimiento :"))

#print(año_de_nacimiento)

#TIPO DE DATO
#print(type(año_de_nacimiento))



#for i in range(0, 11, 2):
#    print(i)

#for i in range(10, 0, -1):
#    print(i)

for i in range(11):
    if i ==5:
        break
    print(i)
    


#condicionales

puntuacion = int(input("ingrese una nota - (0 - 10)"))

if puntuacion >= 9:
    print("Excelente")
elif puntuacion >=7:
    print("Bien")
else:
    print("Desaprobado")

#-------------------#



resultado = 2 + 3
print(resultado)
potencia= 2**3
print(potencia)

result = 5 > 2

licencia = True
not(edad >= 18 and licencia)

#-------------#