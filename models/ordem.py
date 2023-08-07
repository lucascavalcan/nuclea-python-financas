from models.cliente import Cliente
from repository.banco_de_dados import BancoDeDados


class Ordem:

    def __init__(self):
        self.nome = None
        self.ticket = None
        self.valor_compra = None
        self.quantidade_compra = None
        self.data_compra = None
        self.cliente_id = None
        self.banco_de_dados = BancoDeDados()
        self.cliente = Cliente()

    def cadastrar(self, ordem):
        cliente_id = self.buscar_id_por_cpf(ordem['cpf_cliente'])
        if cliente_id is not None:  # Certifique-se de que um ID válido foi encontrado
            ordem['cliente_id'] = cliente_id
            self.banco_de_dados.insert_ordem(ordem)
            print("Ordem cadastrada com sucesso!")
        else:
            print("Cliente não encontrado. Não foi possível cadastrar a ordem.")

    def consultar(self, ticket):
        ordem = self.banco_de_dados.select_ordem(ticket)
        if ordem:
            print("Ordem encontrada:")
            print("Nome:", ordem[0]['nome'])
            print("Ticket:", ordem[0]['ticket'])
            print("Valor da Compra:", ordem[0]['valor_compra'])
            print("Quantidade da Compra:", ordem[0]['quantidade_compra'])
            print("Data da Compra:", ordem[0]['data_compra'])
            print("ID do Cliente:", ordem[0]['cliente_id'])
        else:
            print("Ordem não encontrada.")

    def atualizar(self, ticket, novos_dados):
        ordem = self.banco_de_dados.select_ordem(ticket)
        if ordem:
            novos_dados['ticket'] = ticket
            self.banco_de_dados.update_ordem(novos_dados)
            print("Ordem atualizada com sucesso.")
        else:
            print("Ordem não encontrada.")

    def deletar(self, ticket):
        ordem = self.banco_de_dados.select_ordem(ticket)
        if ordem:
            self.banco_de_dados.delete_ordem(ticket)
            print("Ordem deletada com sucesso.")
        else:
            print("Ordem não encontrada.")

    def buscar_id_por_cpf(self, cpf):
        cliente_id = self.cliente.buscar_id_por_cpf(cpf)
        if cliente_id is not None:  # Certifica-se de que um ID válido foi encontrado
            return cliente_id
        else:
            print("Cliente não encontrado.")
            return None

