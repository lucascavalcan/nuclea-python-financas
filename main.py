from models.cliente import Cliente
from models.ordem import Ordem
from repository.banco_de_dados import BancoDeDados
from utils.cep import valida_cep
from utils.data import valida_data_nascimento
from utils.funcoes_auxiliares import formata_texto, numero_casa
from utils.funcoes_ordem import formata_ticket, valor, quantidade, data_compra
from utils.valida_cpf import valida_cpf
from utils.valida_rg import valida_rg


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
                    cpf_consulta = valida_cpf()
                    cliente.consultar(cpf_consulta)
                elif opcao_cliente == "1":
                    novo_cliente = {
                        "nome": formata_texto(),
                        "cpf": valida_cpf(),
                        "rg": valida_rg(),
                        "data_nascimento": valida_data_nascimento(),
                        "endereço": valida_cep(),
                        'numero_residencia': numero_casa()
                    }
                    cliente.cadastrar(novo_cliente)
                elif opcao_cliente == "3":
                    print("Atualizando cliente...")
                    cpf_att = valida_cpf()
                    novos_dados = {
                        "nome": formata_texto(),
                        "cpf": valida_cpf(),
                        "rg": valida_rg(),
                        "data_nascimento": valida_data_nascimento(),
                        "endereço": valida_cep(),
                        'numero_residencia': numero_casa()
                    }
                    cliente.atualizar(cpf_att, novos_dados)
                elif opcao_cliente == "4":
                    cpf_deletar = valida_cpf()
                    cliente.deletar(cpf_deletar)
                elif opcao_cliente == "5":
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == "2":
            ordem = Ordem()
            while True:
                print("Menu Ordem:")
                print("1 - Cadastrar")

                nova_ordem = {
                    "nome": formata_texto(),
                    "ticket": formata_ticket(),
                    "valor_compra": valor(),
                    "quantidade_compra": quantidade(),
                    "data_compra": data_compra(),
                    "cpf_cliente": input("Digite o CPF do cliente associado à ordem: ")
                }
                cliente_id = ordem.buscar_id_por_cpf(nova_ordem['cpf_cliente'])  # Buscar ID do cliente pelo CPF
                nova_ordem['cliente_id'] = cliente_id  # Adicionar o ID do cliente à ordem
                ordem.cadastrar(nova_ordem)


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
