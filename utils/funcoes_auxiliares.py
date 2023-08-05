def retorna_menu_principal():
    while True:
        retorna_menu_principal = input("Deseja retornar ao menu principal? (sim/não): ")
        if retorna_menu_principal == "sim":
            return True
        elif retorna_menu_principal == "nao" or "não":
            return False
        else:
            print("Valor inválido. Digite apenas 'sim' ou 'não'.")


def formata_texto():
    while True:
        nome = input("Nome: ")
        nome_formatado = nome.title()
        return nome_formatado

def numero_casa():
    while True:
        casa = int(input("Número da Casa: "))
        return casa

def nome_arquivo():
    while True:
       arquivo = input("Digite o nome do arquivo de saída (ex: relatorio_acao.txt): ").strip()
       return arquivo
