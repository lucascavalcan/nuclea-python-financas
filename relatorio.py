import yfinance as yf

def obter_dados_acao(ticket, nome_arquivo):

    try:

        print("Coletando dados da ação: " + ticket)

        acao = yf.download(ticket + '.SA', progress=False)

        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write("Relatório da ação: " + ticket + "\n")
            arquivo.write(str(acao.tail()))
            arquivo.close()


    except Exception as e:
        print("Erro ao obter dados da ação. Verifique se o seu nome está correto.")


ticket = input("Digite o nome da ação: ")
nome_arquivo = input("Digite o nome do arquivo: ")
obter_dados_acao(ticket, nome_arquivo)