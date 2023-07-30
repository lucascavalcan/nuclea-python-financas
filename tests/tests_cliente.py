import unittest
from unittest.mock import patch

from faker import Faker
from validate_docbr import CPF

from main import main, clientes


def gera_cpf():
    cpf = CPF()
    cpf_gerado = cpf.generate()
    return cpf_gerado


class TestStringMethods(unittest.TestCase):

    def gerar_nome_fake(self):
        fake = Faker()
        return fake.name()


    def test_cliente(self):
        nome = self.gerar_nome_fake()
        cpf = gera_cpf()
        inputs = ["1", nome, cpf, "12.345.678-x", "06/03/1998", "58046780", "701", "nao"]

        with patch("builtins.input", side_effect=inputs):
            main()

        cliente_esperado = {
            "nome": nome,
            "cpf": f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}",
            "rg": "12.345.678-x",
            "data_nascimento": "06/03/1998",
            "endereco": {'CEP': '58046-780', 'Logradouro': 'Rua Ana de Fátima Gama Cabral',
                         'Complemento': '(Lot Q Mares II)', 'Bairro': 'Portal do Sol', 'Cidade': 'João Pessoa', 'Estado': 'PB'},
            "numero_casa": "701",
        }

        self.assertIn(cliente_esperado, clientes)
