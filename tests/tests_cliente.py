import unittest
from unittest.mock import patch

from faker import Faker
from validate_docbr import CPF

from models.cliente import Cliente

class TestCliente(unittest.TestCase):

    def gera_cpf(self):
        cpf = CPF()
        cpf_gerado = cpf.generate()
        return cpf_gerado

    def gerar_nome_fake(self):
        fake = Faker()
        return fake.name()

    def test_cliente(self):
        cliente_instance = Cliente()

        cpf = self.gera_cpf()
        # Dados fictícios para simular a entrada do usuário
        inputs = ["1", "1", "Fulano de Tal", "938.188.544-99", "12.345.678-x", "06/03/1998", "58046780", "701"]

        with patch("builtins.input", side_effect=inputs):
            cliente = {
                "nome": "Fulano de Tal",
                "cpf": f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}",
                "rg": "12.345.678-x",
                "data_nascimento": "06/03/1998",
                "endereço": {'CEP': '58046-780', 'Logradouro': 'Rua Ana de Fátima Gama Cabral',
                             'Complemento': '(Lot Q Mares II)', 'Bairro': 'Portal do Sol', 'Cidade': 'João Pessoa',
                             'Estado': 'PB'},
                "numero_residencia": "701",
            }
            cliente_instance.cadastrar(cliente)

        # Simular a consulta do cliente
        cpf_consulta = "938.188.544-99"
        cpf_consulta_formatado = cpf_consulta.replace(".", "").replace("-", "")
        dados_cliente = cliente_instance.consultar(cpf_consulta_formatado)

        # Dados esperados
        cliente_esperado = {
            "nome": "Fulano de Tal",
            "cpf": f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}",
            "rg": "12.345.678-x",
            "data_nascimento": "06/03/1998",
            "endereço": {'CEP': '58046-780', 'Logradouro': 'Rua Ana de Fátima Gama Cabral',
                         'Complemento': '(Lot Q Mares II)', 'Bairro': 'Portal do Sol', 'Cidade': 'João Pessoa', 'Estado': 'PB'},
            "numero_residencia": "701",
        }

        # Verificar se os dados da consulta são iguais aos dados esperados
        self.assertEqual(dados_cliente['nome'], cliente_esperado['nome'])
        self.assertEqual(dados_cliente['cpf'], cliente_esperado['cpf'])
        self.assertEqual(dados_cliente['rg'], cliente_esperado['rg'])
        self.assertEqual(dados_cliente['data_nascimento'], cliente_esperado['data_nascimento'])
        self.assertEqual(dados_cliente['endereco'], cliente_esperado['endereco'])
        self.assertEqual(dados_cliente['numero_residencia'], cliente_esperado['numero_residencia'])

if __name__ == '__main__':
    unittest.main()
