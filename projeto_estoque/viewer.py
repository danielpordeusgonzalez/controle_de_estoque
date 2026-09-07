import math

import model
import template


def cadastrar_produto():
    nome, preco, quantidade = template.solicitar_dados_produto()
    nome = nome.strip()

    try:
        preco = float(preco.replace(",", "."))
        quantidade = int(quantidade)
    except ValueError:
        template.exibir_resultado_cadastro(False)
        return

    if not nome or not math.isfinite(preco) or preco < 0 or quantidade < 0:
        template.exibir_resultado_cadastro(False)
        return

    model.adicionar_produto(nome, preco, quantidade)
    template.exibir_resultado_cadastro(True)


def listar_produtos():
    if not model.produtos:
        template.exibir_estoque_vazio()
        return

    template.exibir_lista_produtos(model.produtos)


def buscar_produto():
    nome = template.solicitar_nome_produto().strip().lower()

    for produto in model.produtos:
        if produto["nome"].lower() == nome:
            template.exibir_produto(produto)
            return produto

    template.exibir_produto_nao_encontrado()
    return None


def entrada_estoque():
    produto = buscar_produto()
    if produto is None:
        return

    try:
        quantidade = int(template.solicitar_quantidade_entrada())
    except ValueError:
        template.exibir_entrada_invalida()
        return

    if quantidade < 0:
        template.exibir_entrada_invalida()
        return

    produto["quantidade"] += quantidade
    template.exibir_entrada_realizada(produto["quantidade"])


def saida_estoque():
    produto = buscar_produto()
    if produto is None:
        return

    try:
        quantidade = int(template.solicitar_quantidade_saida())
    except ValueError:
        template.exibir_saida_invalida()
        return

    if quantidade < 0:
        template.exibir_saida_invalida()
        return

    if quantidade > produto["quantidade"]:
        template.exibir_estoque_insuficiente()
        return

    produto["quantidade"] -= quantidade
    template.exibir_saida_realizada(produto["quantidade"])


def calcular_valor_estoque():
    valor_total = 0
    for produto in model.produtos:
        valor_produto = produto["preco"] * produto["quantidade"]
        template.exibir_valor_produto(produto["nome"], valor_produto)
        valor_total += valor_produto

    template.exibir_valor_total(valor_total)
    return valor_total


def mostrar_resumo_estoque():
    if not model.produtos:
        template.exibir_estoque_vazio()
        return

    produto_maior_quantidade = model.produtos[0]
    produto_menor_quantidade = model.produtos[0]
    produto_mais_caro = model.produtos[0]
    produtos_estoque_baixo = []

    for produto in model.produtos:
        if produto["quantidade"] > produto_maior_quantidade["quantidade"]:
            produto_maior_quantidade = produto
        if produto["quantidade"] < produto_menor_quantidade["quantidade"]:
            produto_menor_quantidade = produto
        if produto["preco"] > produto_mais_caro["preco"]:
            produto_mais_caro = produto
        if produto["quantidade"] < 5:
            produtos_estoque_baixo.append(produto)

    template.exibir_resumo_estoque(
        produto_maior_quantidade,
        produto_menor_quantidade,
        produto_mais_caro,
        produtos_estoque_baixo,
    )
