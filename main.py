# main.py
# chama as funções criadas no arquivo funcoes.py

from functions_sprint import (
    informacoes,
    cadastrar_informacao,
    listar_informacoes,
    pesquisar_por_tipo
)

while True:
    print("=== Totem FlexMedia ===")
    print("1 - Cadastrar informação")
    print("2 - Listar informações cadastradas")
    print("3 - Pesquisar informações por tipo")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        cadastrar_informacao(informacoes)

    elif opcao == "2":
        listar_informacoes(informacoes)

    elif opcao == "3":
        pesquisar_por_tipo(informacoes)

    elif opcao == "0":
        print("\nEncerrando o programa.")
        break

    else:
        print("\nOpção invalida! Tente novamente.\n")
