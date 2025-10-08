# Este programa define uma classe que solicita dois números, realizar a divisão e trata os erros específicos de divisão por zero e entrada de valores não numéricos.

produtos = []
proximo_id = 1

def adicionar_produto():
    global proximo_id
    nome = input("Digite o nome do produto: ")

    while True:
        try:
            preco = float(input("Digite o preço do produto (ex: 19.99): "))
            break
        except ValueError:
            print("Erro: Preço inválido.")

    produto = {
        'id': proximo_id,
        'nome': nome,
        'preco': preco
    }

    produtos.append(produto)
    proximo_id += 1
    print(f"\nProduto '{nome}' adicionado com sucesso!")

def visualizar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado no momento.")
    else:
        print(f"{'ID':<5} | {'Nome':<20} | {'Preço (R$)'}")
        for produto in produtos:
            print(f"{produto['id']:<5} | {produto['nome']:<20} | {produto['preco']:.2f}")

def atualizar_produto():
    try:
        id_para_atualizar = int(input("Digite o ID do produto que deseja atualizar: "))
    except ValueError:
        print("ID inválido. Por favor, digite um número.")
        return

    produto_encontrado = None
    for produto in produtos:
        if produto['id'] == id_para_atualizar:
            produto_encontrado = produto
            break

    if produto_encontrado:
        print(f"Produto encontrado: {produto_encontrado['nome']}")
        novo_nome = input(f"Digite o novo nome (ou pressione Enter para manter '{produto_encontrado['nome']}'): ")
        if novo_nome:
            produto_encontrado['nome'] = novo_nome

        while True:
            try:
                novo_preco_str = input(f"Digite o novo preço (ou pressione Enter para manter R${produto_encontrado['preco']:.2f}): ")
                if novo_preco_str:
                    produto_encontrado['preco'] = float(novo_preco_str)
                break
            except ValueError:
                print("Erro: Preço inválido. Tente novamente.")

        print("\nProduto atualizado com sucesso!")
    else:
        print(f"\nProduto com ID {id_para_atualizar} não encontrado.")

def remover_produto():
    try:
        id_para_remover = int(input("Digite o ID do produto que deseja remover: "))
    except ValueError:
        print("ID inválido. Por favor, digite um número.")
        return

    produto_para_remover = None

    for produto in produtos:
        if produto['id'] == id_para_remover:
            produto_para_remover = produto
            break

    if produto_para_remover:
        produtos.remove(produto_para_remover)
        print(f"\nProduto '{produto_para_remover['nome']}' removido com sucesso!")
    else:
        print(f"\nProduto com ID {id_para_remover} não encontrado.")

def mostrar_menu():
    print("Sistema de Gestão de Loja")
    print("1. Adicionar Produto")
    print("2. Visualizar Produtos")
    print("3. Atualizar Produto")
    print("4. Remover Produto")
    print("5. Sair")

while True:
    mostrar_menu()
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        adicionar_produto()
    elif escolha == '2':
        visualizar_produtos()
    elif escolha == '3':
        atualizar_produto()
    elif escolha == '4':
        remover_produto()
    elif escolha == '5':
        print("\nSaindo do sistema. Até logo!")
        break
    else:
        print("\nOpção inválida. Por favor, escolha um número de 1 a 5.")