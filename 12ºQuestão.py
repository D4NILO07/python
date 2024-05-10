import os
os.system("cls || clear")

nome = input("\nDigite seu nome: ")
estadoCivil = input("\nDigite seu estado civil: ")
sexo = input("\nDigite seu sexo - ultilize F ou M: ")

if sexo == "F" and estadoCivil == "Casada":
    anos = int(input("Quantos anos você tem de casada? "))
    print(f"Nome: {nome}")
    print(f"Sexo: {sexo}")
    print(f"Estado Civil: {estadoCivil}")
    print(f"Tempo de casamento: {anos}")
else: 
    print("Tecle enter para encerrar.")


