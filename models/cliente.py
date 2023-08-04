from repository.banco_de_dados import BancoDeDados

class Cliente:

    def __init__(self):
        self.cpf = None
        self.banco_de_dados = BancoDeDados()

    def cadastrar(self, cliente):
        self.banco_de_dados.insert(cliente)
        print("Cliente cadastrado com sucesso.")

    def consultar(self, cpf):
        cliente = self.banco_de_dados.select({"cpf": cpf})
        if cliente:
            print("Cliente encontrado:")
            print("Nome:", cliente['nome'])
            print("CPF:", cliente['cpf'])
            print("RG:", cliente['rg'])
            print("Data de Nascimento:", cliente['data_nascimento'])
            print("CEP:", cliente['cep']['CEP'])
            print("Logradouro:", cliente['cep']['logradouro'])
            print("Complemento:", cliente['cep']['complemento'])
            print("Bairro:", cliente['cep']['bairro'])
            print("Cidade:", cliente['cep']['cidade'])
            print("Estado:", cliente['cep']['estado'])
            print("Número da Casa:", cliente['numero_residencia'])
        else:
            print("Cliente não encontrado.")

    def atualizar(self, cpf, novos_dados):
        cliente = self.banco_de_dados.select({"cpf": cpf})
        if cliente:
            cliente.update(novos_dados)
            self.banco_de_dados.update(cliente)
            print("Cliente atualizado com sucesso.")
        else:
            print("Cliente não encontrado.")

    def deletar(self, cpf):
        cliente = self.banco_de_dados.select({"cpf": cpf})
        if cliente:
            self.banco_de_dados.delete({"cpf": cpf})
            print("Cliente deletado com sucesso.")
        else:
            print("Cliente não encontrado.")
