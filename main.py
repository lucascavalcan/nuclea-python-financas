from models.cliente import Cliente
from models.ordem import Ordem
from repository.banco_de_dados import BancoDeDados
from utils.funcoes_auxiliares import formata_texto

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
            cliente = Cliente()
            while True:
                print("Menu Cliente:")
                print("1 - Cadastrar")
                print("2 - Consultar")
                print("3 - Atualizar")
                print("4 - Deletar")
                print("5 - Voltar ao menu principal")

                opcao_cliente = input("Digite a opção desejada: ")

                if opcao_cliente == "2" or len(opcao_cliente) == 14:
                    cliente.consultar()
                elif opcao_cliente == "1":
                    novo_cliente = {
                        'nome': input("Nome: "),
                        'cpf': input("CPF: "),
                        'rg': input("RG: "),
                        'data_nascimento': input("Data de Nascimento: "),
                        'cep': {
                            'CEP': input("CEP: "),
                            'logradouro': input("Logradouro: "),
                            'complemento': input("Complemento: "),
                            'bairro': input("Bairro: "),
                            'cidade': input("Cidade: "),
                            'estado': input("Estado: "),
                        },
                        'numero_residencia': input("Número da Casa: ")
                    }
                    cliente.cadastrar(novo_cliente)
                elif opcao_cliente == "3":
                    cliente.atualizar()
                elif opcao_cliente == "4":
                    cliente.deletar()
                elif opcao_cliente == "5":
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == "2":
            ordem = Ordem()
            while True:
                print("Menu Ordem:")
                print("1 - Cadastrar")
                print("2 - Consultar")
                print("3 - Atualizar")
                print("4 - Deletar")
                print("5 - Voltar ao menu principal")

                opcao_ordem = input("Digite a opção desejada: ")

                if opcao_ordem == "2" or len(opcao_ordem) == 14:
                    ordem.consultar()
                elif opcao_ordem == "1":
                    ordem.cadastrar()
                elif opcao_ordem == "3":
                    ordem.atualizar()
                elif opcao_ordem == "4":
                    ordem.deletar()
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
