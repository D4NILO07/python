import os
os.system("cls || clear")

numero = int(input("Digite o 1º Número: "))
numeroDois = int(input("Digite o 2º Número: "))


print("Digite 1 caso queira somar os dois números.")
print("Digite 2 caso queira subtrair os dois números.")
print("Digite 3 caso queira multiplicar os dois números.")
print("Digite 4 caso queira dividir os dois números.")
print("Digite 5 caso queira exibir todos os resultados.")
print("Digite 0 caso queira sair: ")

opcao = int(input("Digite a opção desejada: "))

soma = numero + numeroDois
subtracao = numero - numeroDois
multiplicacao = numero * numeroDois
divisao = numero / numeroDois

match(opcao):
    case 1:
        print("=== EXIBINDO DADOS ===")
        print(f"Soma: {soma}")
    case 2: 
        print("=== EXIBINDO DADOS ===")
        print(f"Subtração: {subtracao}")
    case 3:
        print("=== EXIBINDO DADOS ===")
        print(f"Multiplicação: {multiplicacao}")
    case 4: 
        print("=== EXIBINDO DADOS ===")
        print(f"Divisão: {divisao}")
    case 5:
        print("=== EXIBINDO DADOS ===")
        print(f"Soma: {soma}")
        print(f"Subtração: {subtracao}")
        print(f"Multiplicação: {multiplicacao}")
        print(f"Divisão: {divisao}")
    
    
      