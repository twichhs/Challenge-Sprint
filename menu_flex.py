# Lista que armazena todas as informações cadastradas
informacoes = []  # Aqui vão todas as infos, tipo o HD do Totem 🖥️

def cadastrar_informacao(lista):
    """
    Função responsável por cadastrar uma nova informação no totem.
    Cada informação contém título, tipo e descrição.
    """
    print("\n--- Cadastro de Nova Informação ---")
    # Pega os dados do usuário. Não esquece de digitar certo, senão o Totem vai chorar 😢
    titulo = input("Digite o título: ").strip()
    tipo = input("Digite o tipo (educativo, cultural, lazer etc.): ").strip()
    descricao = input("Digite a descrição: ").strip()

    nova_info = {
        "titulo": titulo,
        "tipo": tipo,
        "descricao": descricao
    }

    lista.append(nova_info)  # Adiciona à lista, tipo colocar na mochila do Totem 🎒
    print("\n✅ Informação cadastrada com sucesso! (O Totem aprovou 😎)\n")

def listar_informacoes(lista):
    """
    Função responsável por exibir todas as informações cadastradas.
    """
    print("\n--- Informações Cadastradas ---")
    if not lista:
        print("Nenhuma informação cadastrada ainda. Totem está vazio 😬")
    else:
        for i, info in enumerate(lista, start=1):
            print(f"\nInformação {i}:")
            print(f"📌 Título: {info['titulo']}")
            print(f"📂 Tipo: {info['tipo']}")
            print(f"📝 Descrição: {info['descricao']}")
    print()  # linha em branco final, porque ninguém gosta de bagunça 😅

# --- Programa Principal ---
while True:
    print("=== Totem FlexMedia ===")
    print("1 - Cadastrar informação")
    print("2 - Listar informações cadastradas")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    # Se liga nas opções! É tipo GPS do Totem 🚗
    if opcao == "1":
        cadastrar_informacao(informacoes)
    elif opcao == "2":
        listar_informacoes(informacoes)
    elif opcao == "0":
        print("\n👋 Encerrando o programa. Até mais! (O Totem vai tirar um cochilo 💤)")
        break
    else:
        print("\n⚠️ Opção inválida! Tente novamente. (Totem não entende alienígena 👽)\n")