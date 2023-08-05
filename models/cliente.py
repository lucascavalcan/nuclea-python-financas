from repository.banco_de_dados import BancoDeDados

class Cliente:

    def __init__(self):
        self.cpf = None
        #inicializar tambem os outros valores como None
        self.banco_de_dados = BancoDeDados()


    def cadastrar(self, cliente):
        self.banco_de_dados.insert(cliente)
        print("Cliente cadastrado com sucesso.")

    def consultar(self, cpf):
        clientes = self.banco_de_dados.select({"cpf": cpf})
        if clientes:
            cliente = clientes[0]  # Pega a primeira tupla (primeiro cliente)
            print("Cliente encontrado:")
            print("Nome:", cliente[1])  # Índice 1 representa o nome
            print("CPF:", cliente[2])  # Índice 2 representa o CPF
            print("RG:", cliente[3])  # Índice 3 representa o RG
            print("Data de Nascimento:", cliente[4])  # Índice 4 representa a data de nascimento
            print("CEP:", cliente[5])  # Índice 5 representa o CEP
            print("Logradouro:", cliente[6])  # Índice 6 representa o logradouro
            print("Complemento:", cliente[7])  # Índice 7 representa o complemento
            print("Bairro:", cliente[8])  # Índice 8 representa o bairro
            print("Cidade:", cliente[9])  # Índice 9 representa a cidade
            print("Estado:", cliente[10])  # Índice 10 representa o estado
            print("Número da Casa:", cliente[11])  # Índice 11 representa o número da casa
        else:
            print("Cliente não encontrado.")

    def atualizar(self, cpf, novos_dados):
        clientes = self.banco_de_dados.select({"cpf": cpf})
        if clientes:
            cliente_tuple = clientes[0]  # Pega a primeira tupla (primeiro cliente)
            cliente_dict = {
                "nome": cliente_tuple[1],
                "cpf": cliente_tuple[2],
                "rg": cliente_tuple[3],
                "data_nascimento": cliente_tuple[4],
                "endereço": {
                    "CEP": cliente_tuple[5],
                    "Logradouro": cliente_tuple[6],
                    "Complemento": cliente_tuple[7],
                    "Bairro": cliente_tuple[8],
                    "Cidade": cliente_tuple[9],
                    "Estado": cliente_tuple[10]
                },
                "numero_residencia": cliente_tuple[11]
            }
            # Atualize os campos de endereço individualmente
            if 'endereço' in novos_dados:
                for campo_endereco in novos_dados['endereço']:
                    cliente_dict['endereço'][campo_endereco] = novos_dados['endereço'][campo_endereco]

            cliente_dict.update(novos_dados)
            self.banco_de_dados.update(cliente_dict)
        else:
            print("Cliente não encontrado.")

    def deletar(self, cpf):
        cliente = self.banco_de_dados.select({"cpf": cpf})
        if cliente:
            self.banco_de_dados.delete({"cpf": cpf})
        else:
            print("Cliente não encontrado.")

    def buscar_id_por_cpf(self, cpf):
        cliente_id = self.banco_de_dados.buscar_id_por_cpf(cpf)
        return cliente_id