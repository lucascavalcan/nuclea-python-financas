import psycopg2
import os

class BancoDeDados:

    def __init__(self):
        self.connection = psycopg2.connect(**self.retorna_parametros_conexao_banco_de_dados())
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def insert(self, cliente):
        print("Inserindo cliente no banco de dados: ")
        insert_query = """
                INSERT INTO cliente (nome, cpf, rg, data_nascimento, cep, logradouro, complemento,
	            bairro, cidade, estado, numero_residencia)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                """
        values = (
            cliente['nome'],
            cliente['cpf'],
            cliente['rg'],
            cliente['data_nascimento'],
            cliente['endereço']['CEP'],
            cliente['endereço']['Logradouro'],
            cliente['endereço']['Complemento'],
            cliente['endereço']['Bairro'],
            cliente['endereço']['Cidade'],
            cliente['endereço']['Estado'],
            cliente['numero_residencia']
        )
        self.cursor.execute(insert_query, values)
        self.connection.commit()

    def select(self, cliente):
        print("Selecionando cliente no banco de dados...")
        select_query = "SELECT * FROM cliente WHERE cpf = %s;"
        self.cursor.execute(select_query, (cliente['cpf'],))
        clientes = self.cursor.fetchall()
        #for cliente in clientes:
        #    print(cliente)
        return clientes

    def delete(self, cliente):
        print("Deletando cliente do banco de dados: ")
        delete_query = "DELETE FROM cliente WHERE cpf = %s;"
        self.cursor.execute(delete_query, (cliente['cpf'],))
        self.connection.commit()
        print("Cliente deletado com sucesso.")

    def update(self, cliente):
        print("Atualizando cliente no banco de dados: ")
        update_query = """
            UPDATE cliente
            SET nome = %s, cpf = %s, rg = %s, data_nascimento = %s,
                cep = %s, logradouro = %s, complemento = %s,
                bairro = %s, cidade = %s, estado = %s, numero_residencia = %s
            WHERE cpf = %s;
            """
        values = (
            cliente['nome'],
            cliente['cpf'],
            cliente['rg'],
            cliente['data_nascimento'],
            cliente['endereço']['CEP'],
            cliente['endereço']['Logradouro'],
            cliente['endereço']['Complemento'],
            cliente['endereço']['Bairro'],
            cliente['endereço']['Cidade'],
            cliente['endereço']['Estado'],
            cliente['numero_residencia'],
            cliente['cpf']  # Condição para atualização
        )
        self.cursor.execute(update_query, values)
        self.connection.commit()
        print("Cliente atualizado com sucesso.")

    def insert_ordem(self, ordem):
        print("Inserindo ordem no banco de dados: ")
        insert_query = """
            INSERT INTO ordem (nome, ticket, valor_compra, quantidade_compra, data_compra, cliente_id)
            VALUES (%s, %s, %s, %s, %s, %s);
        """
        values = (
            ordem['nome'],
            ordem['ticket'],
            ordem['valor_compra'],
            ordem['quantidade_compra'],
            ordem['data_compra'],
            ordem['cliente_id']
        )
        self.cursor.execute(insert_query, values)
        self.connection.commit()

    def select_ordem(self, ticket):
        print("Selecionando ordem no banco de dados: ")
        select_query = "SELECT * FROM ordem WHERE ticket = %s;"
        self.cursor.execute(select_query, (ticket,))
        ordens = self.cursor.fetchall()
        for ordem in ordens:
            print(ordem)
        return ordens

    def delete_ordem(self, ticket):
        print("Deletando ordem do banco de dados: ")
        delete_query = "DELETE FROM ordem WHERE ticket = %s;"
        self.cursor.execute(delete_query, (ticket,))
        self.connection.commit()
        print("Ordem deletada com sucesso.")

    def update_ordem(self, ordem):
        print("Atualizando ordem no banco de dados: ")
        update_query = """
            UPDATE ordem
            SET nome = %s, ticket = %s, valor_compra = %s, quantidade_compra = %s,
                data_compra = %s, cliente_id = %s
            WHERE ticket = %s;
        """
        values = (
            ordem['nome'],
            ordem['ticket'],
            ordem['valor_compra'],
            ordem['quantidade_compra'],
            ordem['data_compra'],
            ordem['cliente_id'],
            ordem['ticket']  # Condição para atualização
        )
        self.cursor.execute(update_query, values)
        self.connection.commit()
        print("Ordem atualizada com sucesso.")

    def buscar_id_por_cpf(self, cpf):
        print("Buscando ID do cliente pelo CPF no banco de dados...")
        select_query = "SELECT id FROM cliente WHERE cpf = %s;"
        self.cursor.execute(select_query, (cpf,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

    @staticmethod
    def retorna_parametros_conexao_banco_de_dados():
        parametros_conexao = {
            "user": os.getenv('user'),
            "password": os.getenv('password'),
            "host": os.getenv('host'),
            "port": os.getenv('port'),
            "database": os.getenv('database')
        }

        return parametros_conexao


# Realizar integração com a classe cliente.
conexao = BancoDeDados()
cliente = {"cpf": "914.566.460-95"}
