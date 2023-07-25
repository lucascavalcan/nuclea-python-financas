def retorna_menu_principal():
    retorna_menu_principal = input("Deseja retornar ao menu principal? (sim/não ): ")
    if retorna_menu_principal == "sim":
        retorna_menu = True
        validador = True
    elif retorna_menu_principal == "nao":
        retorna_menu = False


def formata_texto(texto):
    nome_formatado = texto.title()
    return nome_formatado