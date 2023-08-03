class Ordem:

    def __init__(self):
        self.atributos = None
        self.id_cliente = None

    def cadastrar_ordem(self, cliente): # pensar em como vai receber o cliente aqui
        self.id_cliente = cliente #consultar o id do cliente de alguma forma