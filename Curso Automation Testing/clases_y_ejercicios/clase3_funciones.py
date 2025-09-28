# FUNCIONES #

def saludo():
    print('hola')
    
saludo()
saludo()

def saludo(nombre):
    print(f"Hola {nombre}")
    
saludo("Javi")
saludo("Tigger")


def saludo(nombre):
    return (f"Hola {nombre}")
    
print(saludo("genio"))

#CALCULADORA
#FUNCION ANIDADA


def sumar( a , b ):
    return a + b

def calculadora_simple(operacion , a, b ):
    if operacion == 'sumar':
        return sumar(a,b)
    else:
        return 'Operación No Válida'


print(calculadora_simple("sumar",7,2))



try:
    resultado = 10 / 0
except ZeroDivisionError:
    print(f"No se puede dividir por 0")
    
# OTRA FORMA SERIA ASI:

try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")

try:
    resultado = int('abc')
except ValueError as e:
    print(f"Error: {e}")


persona = {
    "nombre" : "Javier",
    "edad" : 49
}

try:
    print(persona ['DNI'])
except KeyError as e:
    print('La clave no existe')


# AFTER CLASE 3 #

usuarios ={
    "Ana":{"edad":56},
    "Jose":{"edad":40},
    "Javo":{"edad":49}
}

def pedir_nombre():
    try:
        nombre = input('Ingrese el Nombre: ')
        edad = usuarios [nombre]["edad"]
        print(f'{nombre} tiene {edad} años')
    except KeyError:
        print(f'ERROR : No se encontró la edad para ese nombre')

pedir_nombre()


try:
    edad = int(input('Ingresa tu edad: '))
    print(f'El año que viene tendrás {edad + 1} años')
except ValueError:
    print('Deves ingresar solo valores uméricos')
