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
else 
    resultado = "Operación Invalida" print(resultado)



