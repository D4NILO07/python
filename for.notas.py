import os
os.system("cls || clear")


soma = 0 

for i in range(1,3):
    while True :
        numero = float(input(f"Digite a sua nota: "))
        if numero < 0 or numero > 10:
            print("Nota inválida... \n")
        else:
            soma = soma + numero 
            break
            
media = soma/2

    
print(f"Média: {media}")