from adicionar import adicionar
from remover import remover
from listar import listar
from editar import editar

# ===== PROGRAMA PRINCIPAL - ja pronto, nao altere =====
inventario = [
    ["espada", 1, "comum"],
    ["pocao", 5, "comum"],
]

opcao = ""
while opcao != "0":
    print("1-adicionar 2-remover")
    print("3-listar 4-editar 0-sair")
    opcao = input("Opcao: ")
    if opcao == "1":
        item = input("Item: ")
        qtd = int(input("Quantidade: "))
        raridade = input("Raridade: ")
        adicionar(inventario, item, qtd, raridade)
    elif opcao == "2":
        i = int(input("Posicao: "))
        remover(inventario, i)
    elif opcao == "3":
        listar(inventario)
    elif opcao == "4":
        i = int(input("Posicao: "))
        qtd = int(input("Nova quantidade: "))
        editar(inventario, i, qtd)
