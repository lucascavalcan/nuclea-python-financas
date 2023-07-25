import re

def valida_rg():

    while True:
        rg = input("RG: ")
        #padrao_rg = r'^\d{2}\.\d{3}\.\d{3}-[0-9A-Za-z]$'
        padrao_rg = '^[0-9A-Za-z.-]{1,20}$'


        if re.match(padrao_rg, rg):
            rg = ''.join(filter(str.isalnum, rg))

            if len(rg) == 9:  # Formato: XXXXXXXXX
                rg_formatado = f"{rg[:2]}.{rg[2:5]}.{rg[5:8]}-{rg[8:]}"
            elif len(rg) == 10:  # Formato: XX.XXXXXXX
                rg_formatado = f"{rg[:2]}.{rg[2:]}-{rg[9:]}"
            else:
                rg_formatado = rg  # Não foi possível formatar, retorna o valor original

            return rg_formatado

        else:
            print("RG inválido, digite novamente: ")
