import os
os.system("cls || clear")

numeros = []

for i in range (5):
    numero = int(input(f"Digite o {i+1}º inteiro: "))
    numeros.append(numero)

    par = []
    impar = []
    
for numero in numeros: 
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print(f"Números pares: {par}")
print(f"Números Ímpares: {impar}")
