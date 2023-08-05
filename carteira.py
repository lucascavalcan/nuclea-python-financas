import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

from repository.banco_de_dados import BancoDeDados


def realizar_analise_carteira(cpf):
    # Conectar ao banco de dados
    banco_de_dados = BancoDeDados()

    # Obter as ordens do cliente a partir do CPF
    ordens = banco_de_dados.select_ordem(cpf)

    if not ordens:
        print("Cliente não possui ordens registradas.")
        return

    # Definir o período de data desejado
    start_date = "2020-01-01"
    end_date = "2023-01-01"

    # Criar um DataFrame vazio
    df = pd.DataFrame()

    # Baixar os dados para cada ação e adicionar ao DataFrame
    for ordem in ordens:
        ticker = ordem[2] + '.SA'  # Assumindo que o ticker está na terceira coluna
        cotacao = yf.download(ticker, start=start_date, end=end_date)
        df[ticker] = cotacao['Adj Close']

    # Plotar as séries de preços do DataFrame
    df.plot(figsize=(15, 10))

    plt.xlabel('Anos')
    plt.ylabel('Valor Ticket')
    plt.title('Variação de valor das ações')
    plt.legend()
    plt.show()

