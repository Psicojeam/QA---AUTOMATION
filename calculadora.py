#CALCULADORA
#FUNCION ANIDADA


def sumar( a , b ):
    return a + b

def restar( a , b ):
    return a - b

def multiplicar( a , b ):
    return a * b

def dividir( a , b ):
    return a // b # Al poner doble / devuelve solo la parte entera
#
#    if b == 0:
#        raise ValueError('Error, no se puede dividir por 0')
#    return a / b

def calculadora_simple(operacion , a, b ):
    try:
        a = int(a)
        b = int(b)

        if operacion == 'sumar':
            return sumar(a,b)
        elif operacion == 'restar':
            return restar(a,b)
        elif operacion == 'multiplicar':
            return multiplicar(a,b)
        elif operacion == 'dividir':
            return dividir(a,b)
        else:
            return KeyError('Operación No Válida')
        
    except ZeroDivisionError:
        return 'No se puede dividir por 0'
    except ValueError:
        return 'Los valores deben ser numéricos'
    
print(calculadora_simple('sumar',1,1)) # 2
print(calculadora_simple('restar',1,1)) # 0
print(calculadora_simple('dividir',1,1)) # 1
print(calculadora_simple('dividir',1,0)) # Error ZeroDivision
print(calculadora_simple('dividir','R',0)) # Error ValueError
print(calculadora_simple('multiplicarabana',5,4)) # Error KeyError



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



#OTRA OPCION A VERIFICAR

num_1 = float(input("Introduce el primer número par realizar la operación : "))
num_2 = float(input("Introduce el segundo número par realizar la operación : "))
operacion = input("Introduce la operación que deseas realizar (+, -, *, /): ")

if operacion == '+':
    resultado = num_1 + num_2
elif operacion == '-':
    resultado = num_1 - num_2
elif operacion == '*':
    resultado = num_1 * num_2
elif operacion == '/':
    resultado = num_1 / num_2
else:
    resultado = "Operación Invalida" 
    print(resultado)



