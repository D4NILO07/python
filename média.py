import os
os.system("cls || clear")

print("Solicitando dados para o usuário.")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
notaUm = float(input("Digite sua 1º Nota: "))
notaDois = float(input("Digite sua 2º Nota: "))

media = (notaUm + notaDois) / 2

print("\nExibindpo dados do usuário.")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"1ª Nota: {notaUm}")
print(f"2ª Nota: {notaDois}")
print(f"Média: {media}")
