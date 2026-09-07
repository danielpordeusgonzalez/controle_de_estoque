produtos = []


def adicionar_produto(nome, preco, quantidade):
    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade,
    }
    produtos.append(produto)
