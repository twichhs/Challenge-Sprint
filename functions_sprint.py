# funcoes.py
# Aqui ficam todas as funções que o Totem usa para funcionar
# Modularização é vida

informacoes = []

TIPOS_VALIDOS = ["educativo", "cultural", "lazer"]

def validar_tipo():
    """
    Obriga o usuário a digitar um tipo válido.
    """
    while True:
        tipo = input("Digite o tipo (educativo / cultural / lazer): ").strip().lower()

        if tipo in TIPOS_VALIDOS:
            return tipo
        else:
            print("Tipo inválido! Tente novamente...")

def cadastrar_informacao(lista):
    print("\n--- Cadastro de Nova Informação ---")

    # Validação do título
    while True:
        titulo = input("Digite o título: ").strip()
        if titulo != "":
            break
        print("O título não pode estar vazio")

    # Validação do tipo
    tipo = validar_tipo()

    # Descrição não precisa de validação obrigatória
    descricao = input("Digite a descrição: ").strip()

    nova_info = {
        "titulo": titulo,
        "tipo": tipo,
        "descricao": descricao
    }

    lista.append(nova_info)
    print("\nInformação cadastrada com sucesso!\n")


def listar_informacoes(lista):
    print("\n--- Informações Cadastradas ---")

    if not lista:
        print("Nenhuma informação cadastrada ainda.")
        return

    for i, info in enumerate(lista, start=1):
        print(f"\nInformação {i}:")
        print(f"📌 Título: {info['titulo']}")
        print(f"📂 Tipo: {info['tipo']}")
        print(f"📝 Descrição: {info['descricao']}")

    print()


def pesquisar_por_tipo(lista):
    print("\n--- Pesquisa por Tipo ---")

    tipo = validar_tipo()

    encontrados = [info for info in lista if info["tipo"] == tipo]

    if not encontrados:
        print(f"\nNenhuma informação do tipo '{tipo}' foi encontrada.")
        return

    print(f"\nInformações do tipo '{tipo}':")
    for info in encontrados:
        print(f"\n📌 Título: {info['titulo']}")
        print(f"📝 Descrição: {info['descricao']}")

    print()
