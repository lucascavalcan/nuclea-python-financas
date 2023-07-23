validador = True
clientes = []

while(validador):
    print("Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea. Selecione uma das opções abaixo: ")
    print("1 - Cadastrar cliente")
    print("2 - Cadastrar ação")
    print("3 - Realizar análise de carteira")
    print("4 - Imprimir relatório da carteira")
    print("5 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        print("Informe os dados do cliente: ")
        cliente = {
            "nome": input("Nome: "),
            "cpf": input("CPF: "),
            "rg": input("RG: "),
            "data_nascimento": input("Data de nascimento: "),
            "cep": input("CEP: "),
            "numero_casa": input("Número casa: ")
        }
        clientes.append(cliente)
        print(clientes)
    elif opcao == "2":
        pass
    elif opcao == "3":
        pass
    elif opcao == "4":
        pass
    elif opcao == "5":
        print("Obrigado por utilizar o sistema de gerenciamento de carteira de ações da Nuclea. Até a próxima!")
        validador = False
    else:
        print("Opção inválida. Tente novamente.")