import unittest
from unittest.mock import patch

from faker import Faker

from main import main, clientes
from utils.valida_cpf import gera_cpf


class TestStringMethods(unittest.TestCase):

    def gerar_nome_fake(self):
        fake = Faker()
        return fake.name()

    def test_cliente(self):
        nome = self.gerar_nome_fake()
        cpf = gera_cpf()
        inputs = ["1", nome, cpf, "12.345.678-x", "06/03/1998", "58046780", "701", "nao"]

        with patch("builtins.input", sife_effect=inputs):
            main()

        cliente_esperado = {
            "nome": nome,
            "cpf": f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}",
            "rg": "12.345.678-x",
            "data_nascimento": "06/03/1998",
            "endereco": {'cep': '58046-780', 'logradouro': 'Rua Ana de Fátima Gama Cabral',
                         'complemento': '(Lot Q Mares II)', 'bairro': 'Portal do Sol', 'cidade': 'João Pessoa', 'uf': 'PB'},
            "numero_casa": "701",
        }

        self.assertIn(cliente_esperado, clientes)
