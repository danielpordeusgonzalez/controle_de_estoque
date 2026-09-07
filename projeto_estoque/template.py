def exibir_titulo():
    print("===== SISTEMA DE ESTOQUE =====")


def exibir_menu():
    print()
    exibir_titulo()
    print("\n1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Entrada de estoque")
    print("5 - Saída de estoque")
    print("6 - Mostrar valor total do estoque")
    print("7 - Mostrar resumo do estoque")
    print("0 - Sair")


def solicitar_opcao():
    return input("\nEscolha uma opção: ").strip()


def exibir_opcao_invalida():
    print("Opção inválida. Escolha uma das opções do menu.")


def exibir_encerramento():
    print("Sistema encerrado.")


def solicitar_dados_produto():
    print("\n===== CADASTRAR PRODUTO =====")
    nome = input("Nome do produto: ")
    preco = input("Preço (R$): ")
    quantidade = input("Quantidade: ")
    return nome, preco, quantidade


def exibir_resultado_cadastro(sucesso):
    if sucesso:
        print("Produto cadastrado com sucesso.")
    else:
        print(
            "Cadastro não realizado. Informe um nome, um preço válido não negativo "
            "e uma quantidade inteira não negativa."
        )


def formatar_preco(valor):
    valor_formatado = f"{valor:,.2f}"
    valor_formatado = valor_formatado.replace(",", "_").replace(".", ",").replace("_", ".")
    return f"R$ {valor_formatado}"


def exibir_produto(produto):
    print(f"\nProduto: {produto['nome']}")
    print(f"Preço: {formatar_preco(produto['preco'])}")
    print(f"Quantidade: {produto['quantidade']}")


def exibir_lista_produtos(produtos):
    print("\n===== PRODUTOS CADASTRADOS =====")
    for produto in produtos:
        exibir_produto(produto)


def exibir_estoque_vazio():
    print("O estoque está vazio.")


def solicitar_nome_produto():
    return input("Nome do produto a buscar: ")


def exibir_produto_nao_encontrado():
    print("Produto não encontrado.")


def solicitar_quantidade_entrada():
    return input("Quantidade a adicionar: ")


def exibir_entrada_invalida():
    print("Entrada não realizada. Informe uma quantidade inteira não negativa.")


def exibir_entrada_realizada(quantidade_atual):
    print("Entrada de estoque realizada com sucesso.")
    print(f"Nova quantidade: {quantidade_atual}")


def solicitar_quantidade_saida():
    return input("Quantidade a retirar: ")


def exibir_saida_invalida():
    print("Saída não realizada. Informe uma quantidade inteira não negativa.")


def exibir_estoque_insuficiente():
    print("Estoque insuficiente.")


def exibir_saida_realizada(quantidade_atual):
    print("Saída de estoque realizada com sucesso.")
    print(f"Nova quantidade: {quantidade_atual}")


def exibir_valor_produto(nome, valor):
    print(f"{nome}: {formatar_preco(valor)}")


def exibir_valor_total(valor_total):
    print(f"\nValor total do estoque: {formatar_preco(valor_total)}")


def exibir_resumo_estoque(
    produto_maior_quantidade,
    produto_menor_quantidade,
    produto_mais_caro,
    produtos_estoque_baixo,
):
    print("\n===== RESUMO DO ESTOQUE =====")
    print(
        f"Maior quantidade: {produto_maior_quantidade['nome']} "
        f"({produto_maior_quantidade['quantidade']} unidades)"
    )
    print(
        f"Menor quantidade: {produto_menor_quantidade['nome']} "
        f"({produto_menor_quantidade['quantidade']} unidades)"
    )
    print(
        f"Produto mais caro: {produto_mais_caro['nome']} "
        f"({formatar_preco(produto_mais_caro['preco'])})"
    )
    print("\nProdutos com estoque baixo (menos de 5 unidades):")
    if not produtos_estoque_baixo:
        print("Nenhum produto com estoque baixo.")
        return

    for produto in produtos_estoque_baixo:
        exibir_produto(produto)
