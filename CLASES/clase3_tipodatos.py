# LISTAS #
[]

mi_lista = ['Argentina', 232, True]

#la lista comienza en la posición 0, luego 1 y asi sucesivamente (comienza siempre en posición 0)
#SUMAR DATO A MI LISTA
mi_lista.append("dato agregado con .append")
print(mi_lista[3])

#SACAR DATO A MI LISTA

mi_lista.remove(232)
print(mi_lista)
#INSERTAR DATO A MI LISTA (primero va la posición y seundo el dato a insertar)

mi_lista.insert(2, "Segundo Francia")
print(mi_lista)


#----------------------------------------------#

# TUPLAS #
()
mi_tupla = ('Tupla', 666,'Celeste' )
# Son Inmutables
print(mi_tupla)
print(mi_tupla[2])
#---------------------------------------------#

# DICCIONARIO #
{}


persona = {
    "nombre" : "Jaime",
    "apellido" : "Desconocido",
    "edad" : 49
}


print(persona.keys())
print(persona.values())
print(persona.items())

#---------------------------------------------------#
#FOR USADO EN LISTAS

mi_lista = ['Argentina', 232, True]

for i in mi_lista:
    print(i)









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

