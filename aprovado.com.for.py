import os
os.system("cls || clear")

soma = 0
for i in range(3):
    numero = float(input(f"Digite a sua {i+1}ª nota: "))

    soma = soma + numero
    media = soma/4

print(f"Média: {media}")
if media >= 7: 
    print("Aluno Aprovado!!")
if media < 4:
    print("Aluno reprovado!!")
if media < 7 and media > 4:
    print("Aluno em recuperação!!!")


