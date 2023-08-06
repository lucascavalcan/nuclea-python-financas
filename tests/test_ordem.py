import unittest
from unittest.mock import patch
from datetime import date

from faker import Faker

from models.ordem import Ordem


class TestOrdem(unittest.TestCase):

    def gerar_nome_fake(self):
        fake = Faker()
        return fake.name()

    def gerar_valor_compra_fake(self):
        fake = Faker()
        return fake.pydecimal(left_digits=5, right_digits=2, positive=True)

    def gerar_quantidade_compra_fake(self):
        fake = Faker()
        return fake.pydecimal(left_digits=3, right_digits=2, positive=True)

    def test_criar_ordem(self):
        nome_cliente = self.gerar_nome_fake()
        valor_compra = self.gerar_valor_compra_fake()
        quantidade_compra = self.gerar_quantidade_compra_fake()
        data_compra = date.today().strftime('%Y-%m-%d')

        ordem_dados = {
            "nome_cliente": nome_cliente,
            "ticket": "XYZ123",
            "valor_compra": str(valor_compra),
            "quantidade_compra": str(quantidade_compra),
            "data_compra": data_compra,
            "cpf_cliente": "123.456.789-00"
        }

        ordem_instance = Ordem()
        with patch("builtins.input", side_effect=list(ordem_dados.values())):
            ordem_instance.cadastrar(ordem_dados)

        ordem_esperada = {
            "nome": nome_cliente,
            "ticket": "XYZ123",
            "valor_compra": valor_compra,
            "quantidade_compra": quantidade_compra,
            "data_compra": data_compra
        }

        # Verifique se a ordem foi criada corretamente
        self.assertIn(ordem_esperada,
                      ordem_instance.banco_de_dados.select_ordem("123.456.789-00"))  # Passar o CPF válido aqui


if __name__ == "__main__":
    unittest.main()
