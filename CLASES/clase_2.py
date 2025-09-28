

contador = 0
while contador <= 5:
    print(contador)
    contador += 1 

suma = 0 
for i in range(1, 11): # arranca con 1 + suma, luego 2 + suma (que anteriormente dio 1), luego 3 + suma(que habia dado 3) y asi sucesivamente 
    suma += i
    print(f"La suma es: {suma}")

for i in range(10):
    if i == 5:
        break  # Termina el bucle al llegar a 5 
print(i)

for i in range(5):
    if i == 2:
        continue  # Salta la iteración donde i es 2 
print(i)