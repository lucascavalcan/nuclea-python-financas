from utils.cep import valida_cep
from utils.data import valida_data_nascimento
from utils.funcoes_auxiliares import formata_texto, retorna_menu_principal
from utils.valida_cpf import valida_cpf
from utils.valida_rg import valida_rg

clientes = []
ordens = []

def cadastrar_cliente():
    print("Informe os dados do cliente: ")
    cliente = {
        "nome": formata_texto(),
        "cpf": valida_cpf(),
        "rg": valida_rg(),
        "data_nascimento": valida_data_nascimento(),
        "endereco": valida_cep(),
        "numero_residencia": input("Número casa: ")
    }
    clientes.append(cliente)
    print(clientes)


def consultar_cliente():
    cpf_consulta = input("Digite o CPF do cliente que deseja consultar: ")
    cpf_consulta = ''.join(filter(str.isdigit, cpf_consulta))
    encontrado = False

    for cliente in clientes:
        # Modifique esta linha para remover os pontos e traços antes de comparar
        if cliente["cpf"].replace(".", "").replace("-", "") == cpf_consulta:
            print("Cliente encontrado:")
            print("Nome:", cliente["nome"])
            print("CPF:", cliente["cpf"])
            print("RG:", cliente["rg"])
            print("Data de Nascimento:", cliente["data_nascimento"])
            print("CEP:", cliente["endereco"]["CEP"])
            print("Logradouro:", cliente["endereco"]["Logradouro"])
            print("Complemento:", cliente["endereco"]["Complemento"])
            print("Bairro:", cliente["endereco"]["Bairro"])
            print("Cidade:", cliente["endereco"]["Cidade"])
            print("Estado:", cliente["endereco"]["Estado"])
            print("Número da Casa:", cliente["numero_residencia"])
            encontrado = True
            break

    if not encontrado:
        print("Cliente não encontrado.")



def atualizar_cliente():
    cpf_atualizacao = input("Digite o CPF do cliente que deseja atualizar: ")
    cpf_atualizacao = ''.join(filter(str.isdigit, cpf_atualizacao))
    encontrado = False

    for i, cliente in enumerate(clientes):
        if cliente["cpf"].replace(".", "").replace("-", "") == cpf_atualizacao:
            print("Cliente encontrado. Informe os novos dados:")
            clientes[i]["nome"] = formata_texto()
            clientes[i]["cpf"] = valida_cpf()
            clientes[i]["rg"] = valida_rg()
            clientes[i]["data_nascimento"] = valida_data_nascimento()

            endereco = valida_cep()
            clientes[i]["endereco"]["CEP"] = endereco["CEP"]
            clientes[i]["endereco"]["Logradouro"] = endereco["Logradouro"]
            clientes[i]["endereco"]["Complemento"] = endereco["Complemento"]
            clientes[i]["endereco"]["Bairro"] = endereco["Bairro"]
            clientes[i]["endereco"]["Cidade"] = endereco["Cidade"]
            clientes[i]["endereco"]["Estado"] = endereco["Estado"]
            clientes[i]["numero_residencia"] = input("Número casa: ")

            encontrado = True
            break

    if not encontrado:
        print("Cliente não encontrado.")


def deletar_cliente():
    cpf_delecao = input("Digite o CPF do cliente que deseja deletar: ")
    cpf_delecao = ''.join(filter(str.isdigit, cpf_delecao))
    encontrado = False

    for i, cliente in enumerate(clientes):
        if cliente["cpf"].replace(".", "").replace("-", "") == cpf_delecao:
            print("Cliente encontrado e deletado.")
            del clientes[i]
            encontrado = True
            break

    if not encontrado:
        print("Cliente não encontrado.")

def cadastrar_ordem():
    print("Informe os dados da ordem: ")
    ordem = {
        "nome": formata_texto(),
        "ticket": input("Ticket: "),
        "valor_compra": float(input("Valor da compra: ")),
        "quantidade_compra": int(input("Quantidade da compra: ")),
        "data_compra": input("Data da compra: "),
        "cliente_id": input("ID do cliente: ")
    }
    ordens.append(ordem)
    print(ordens)

def consultar_ordem():
    ticket_consulta = input("Digite o Ticket da ordem que deseja consultar: ")
    encontrado = False

    for ordem in ordens:
        if ordem["ticket"] == ticket_consulta:
            print("Ordem encontrada:")
            print("Nome:", ordem["nome"])
            print("Ticket:", ordem["ticket"])
            print("Valor da Compra:", ordem["valor_compra"])
            print("Quantidade da Compra:", ordem["quantidade_compra"])
            print("Data da Compra:", ordem["data_compra"])
            print("ID do Cliente:", ordem["cliente_id"])
            encontrado = True
            break

    if not encontrado:
        print("Ordem não encontrada.")

def atualizar_ordem():
    ticket_atualizacao = input("Digite o Ticket da ordem que deseja atualizar: ")
    encontrado = False

    for i, ordem in enumerate(ordens):
        if ordem["ticket"] == ticket_atualizacao:
            print("Ordem encontrada. Informe os novos dados:")
            ordens[i]["nome"] = formata_texto()
            ordens[i]["ticket"] = input("Ticket: ")
            ordens[i]["valor_compra"] = float(input("Valor da compra: "))
            ordens[i]["quantidade_compra"] = int(input("Quantidade da compra: "))
            ordens[i]["data_compra"] = input("Data da compra: ")
            ordens[i]["cliente_id"] = input("ID do cliente: ")
            encontrado = True
            break

    if not encontrado:
        print("Ordem não encontrada.")

def deletar_ordem():
    ticket_delecao = input("Digite o Ticket da ordem que deseja deletar: ")
    encontrado = False

    for i, ordem in enumerate(ordens):
        if ordem["ticket"] == ticket_delecao:
            print("Ordem encontrada e deletada.")
            del ordens[i]
            encontrado = True
            break

    if not encontrado:
        print("Ordem não encontrada.")

def main():
    validador = True
    while validador:
        print("Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea. Selecione uma das opções abaixo: ")
        print("1 - Cliente")
        print("2 - Ordem")
        print("3 - Realizar análise de carteira")
        print("4 - Imprimir relatório da carteira")
        print("5 - Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            while True:
                print("Menu Cliente:")
                print("1 - Cadastrar")
                print("2 - Consultar")
                print("3 - Atualizar")
                print("4 - Deletar")
                print("5 - Voltar ao menu principal")

                opcao_cliente = input("Digite a opção desejada: ")


                if opcao_cliente == "2" or len(opcao_cliente) == 14:
                    consultar_cliente()
                elif opcao_cliente == "1":
                    cadastrar_cliente()
                elif opcao_cliente == "3":
                    atualizar_cliente()
                elif opcao_cliente == "4":
                    deletar_cliente()
                elif opcao_cliente == "5":
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == "2":
            while True:
                print("Menu Ordem:")
                print("1 - Cadastrar")
                print("2 - Consultar")
                print("3 - Atualizar")
                print("4 - Deletar")
                print("5 - Voltar ao menu principal")

                opcao_ordem = input("Digite a opção desejada: ")


                if opcao_ordem == "2" or len(opcao_ordem) == 14:
                    consultar_ordem()
                elif opcao_ordem == "1":
                    cadastrar_ordem()
                elif opcao_ordem == "3":
                    atualizar_ordem()
                elif opcao_ordem == "4":
                    deletar_ordem()
                elif opcao_ordem == "5":
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == "3":
            pass
        elif opcao == "4":
            pass
        elif opcao == "5":
            print("Obrigado por utilizar o sistema de gerenciamento de carteira de ações da Nuclea. Até a próxima!")
            validador = False
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
