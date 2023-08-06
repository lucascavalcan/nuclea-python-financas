import yfinance as yf
from repository.banco_de_dados import BancoDeDados

def obter_dados_acao(ticket):

    if "." in ticket:
        print(f"Ação {ticket} não é reconhecida pelo Yahoo Finance.")
        return None

    try:
        acao = yf.download(ticket + '.SA', progress=False)
        return acao

    except Exception as e:
        print(f"Erro ao obter dados da ação {ticket}. Detalhes do erro: {e}")
        return None

def imprimir_relatorio_acao(cpf, nome_arquivo):
    banco_de_dados = BancoDeDados()
    acoes = banco_de_dados.select_ordem(cpf)

    if not acoes:
        print("Cliente não possui ordens registradas.")
        return

    with open(nome_arquivo, 'w') as arquivo:
        for acao in acoes:
            ticket = acao[2]
            dados_acao = obter_dados_acao(ticket)

            if dados_acao is not None:
                arquivo.write(f"Relatório da ação {ticket}:\n")
                arquivo.write(str(dados_acao.tail()))
                arquivo.write("\n\n")
                print(f"Relatório para a ação {ticket} exportado com sucesso para o arquivo '{nome_arquivo}'.")

