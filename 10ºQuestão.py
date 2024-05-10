import os
os.system("cls || clear")

print("=== Solicitando dados ===")
nomeProduto = input("Digite o nome do produto: ")
precoProduto = float(input("Digite o preço do produto: C"))
quantidadeProduto = int(input("Digite a quantidade do produto: "))

if quantidadeProduto <= 5: 
    desconto = 0.02
elif quantidadeProduto <= 10:
    desconto = 0.03
else:
    desconto = 0.05

subtotal = precoProduto * quantidadeProduto 
totalPagar = subtotal - (subtotal * desconto)

print("\n=== EXIBINDO RESULTADOS ===")
print(f"Nome do produto: {nomeProduto}")
print(f"Preço do produto: {precoProduto}")
print(f"Quantidade do produto: {quantidadeProduto}")
print(f"Total a pagar: {totalPagar}")

print("=== FIM ===")