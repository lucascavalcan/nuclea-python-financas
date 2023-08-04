from repository.banco_de_dados import BancoDeDados

class Ordem:

    def __init__(self):
        self.banco_de_dados = BancoDeDados()

    def cadastrar(self, ordem):
        self.banco_de_dados.insert_ordem(ordem)
        print("Ordem cadastrada com sucesso.")

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
            novos_dados['ticket'] = ticket  # Garante que o ticket não seja alterado
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
