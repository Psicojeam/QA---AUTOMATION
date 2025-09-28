# RANGE #
#
#range(stop) 10
#range(start, stop) 2 - 11
#range(start, stop, step) 2 - 11 -- 2#
#BUCLES#

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




#-------------#

nombre = "Luis"
edad = 46
altura = 1.76
esMayorDeEdad= True
#Entrada y Salida de datos

print(nombre)

año_de_nacimiento = input("ingresa tu año de nacimiento :")
convertido_a_numero = int(año_de_nacimiento)
print(año_de_nacimiento)

#o de esta forma

año_de_nacimiento = int(input("ingresa tu año de nacimiento :"))

print(año_de_nacimiento)

#TIPO DE DATO
print(type(año_de_nacimiento))

resultado = 2 + 3
print(resultado)
potencia= 2**3
print(potencia)

result = 5 > 2

licencia = True
not(edad >= 18 and licencia)

# WHILE #

i = 1

while i <=5:
    print(i)
    i = i + 1 # ó i +=1
    