import os
os.system("cls || clear")

def inflacionar_preco(preco):
    if preco < 100:
        preco_inflacionado = preco * 1.1  # Inflaciona em 10% se o preço for menor que 100
    else:
        preco_inflacionado = preco * 1.2  # Inflaciona em 20% se o preço for maior ou igual a 100
    return preco_inflacionado

def main():
    preco_produto = float(input("Digite o preço do produto: "))
    preco_inflacionado = inflacionar_preco(preco_produto)
    print("O preço inflacionado do produto é:", preco_inflacionado)

if __name__ == "__main__":
    main()
