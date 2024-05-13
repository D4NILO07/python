import os
os.system("cls || clear")


soma = 0 

for i in range(4):
    numero = float(input(f"Digite a sua {i+1}ª nota: "))

    soma = soma + numero 
    media = soma/4

    
print(f"Média: {media}")