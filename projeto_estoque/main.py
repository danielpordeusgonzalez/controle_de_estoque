import template
import viewer


def main():
    while True:
        template.exibir_menu()
        opcao = template.solicitar_opcao()

        if opcao == "1":
            viewer.cadastrar_produto()
        elif opcao == "2":
            viewer.listar_produtos()
        elif opcao == "3":
            viewer.buscar_produto()
        elif opcao == "4":
            viewer.entrada_estoque()
        elif opcao == "5":
            viewer.saida_estoque()
        elif opcao == "6":
            viewer.calcular_valor_estoque()
        elif opcao == "7":
            viewer.mostrar_resumo_estoque()
        elif opcao == "0":
            template.exibir_encerramento()
            break
        else:
            template.exibir_opcao_invalida()


if __name__ == "__main__":
    main()
