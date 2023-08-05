from datetime import datetime

def formata_texto():
    while True:
        nome = input("Nome: ")
        nome_formatado = nome.title()
        return nome_formatado

def formata_ticket():
    while True:
        nome = input("Ticket: ")
        nome_formatado = nome.upper()
        return nome_formatado

def valor():
    while True:
        valor = float(input("Valor: R$ "))
        return valor

def quantidade():
    while True:
        qtd = int(input("Quantidade: "))
        return qtd

def data_compra():
    while True:
        data = input("Data da compra (dd/mm/yyyy): ")

        try:
            data_convertida = datetime.strptime(data, "%d/%m/%Y").date()
            data_atual = datetime.now().date()

            if data_convertida > data_atual:
                print("A data de compra não pode ser no futuro. Digite novamente.")
            else:
                return data_convertida.strftime("%d/%m/%Y")

        except ValueError as e:
            print("Erro:", e, "Digite novamente a data de compra no formato dd/mm/yyyy")

