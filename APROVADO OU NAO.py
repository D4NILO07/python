import os
os.system("cls || clear")

print("Solicitando dados para o usuário.")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
notaUm = float(input("Digite sua 1º Nota: "))
notaDois = float(input("Digite sua 2º Nota: "))
notaTres = float(input("Digite sua 3º Nota: "))

media = (notaUm + notaDois + notaTres) / 3

print("\nExibindo dados do usuário.")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"1ª Nota: {notaUm}")
print(f"2ª Nota: {notaDois}")
print(f"3ª Nota: {notaTres}")
print(f"Média: {media}")
if media < 7: 
    print("Aluno reprovado.")
else: 
    print("Aluno Aprovado.")