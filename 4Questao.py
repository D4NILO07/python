import os
os.system("cls || clear")

print("Solicitando dados para o usuário.")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
numeroUm = int(input("Digite o 1º Número inteiro: "))
numeroDois = int(input("Digite o 2º Número inteiro: "))

soma = (numeroUm + numeroDois)
multiplicacao = (numeroUm * numeroDois)
media = (numeroUm + numeroDois) / 2
if numeroUm > numeroDois:
    maior = numeroUm
else:
    maior = numeroDois

if numeroUm < numeroDois:
    menor = numeroUm
else: 
    menor = numeroDois
    
print("\nExibindo dados do usuário.")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"1º numero: {numeroUm}")
print(f"2º numero: {numeroDois}")
print(f"Soma: {soma}")
print(f"Multiplicação: {multiplicacao}")
print(f"Média: {media}")
print(f"Maior Número: {maior}")
print(f"Menor Número: {menor}")



