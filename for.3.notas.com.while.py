import os
os.system("cls || clear")


soma = 0 

for i in range(3):
    while True :
        numero = float(input(f"Digite a sua nota: "))
        if numero < 0 or numero > 10:
            print("Nota inválida... \n")
        else:
            soma = soma + numero 
            break
            
media = soma/3

print(f"Média: {media}")
if media >= 7: 
    print("Aluno Aprovado!!")
if media < 5:
    print("Aluno reprovado!!")
if media < 7 and media > 5:
    print("Aluno em recuperação!!!")