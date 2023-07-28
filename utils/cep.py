import requests

def busca_cep(cep):
    url = f"http://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url).json()
    return response

def valida_cep():
    while True:
        cep = input("Digite o CEP para busca: ")
        cep = ''.join(filter(str.isdigit, cep))

        if len(cep) == 8 and cep.isdigit():
            response = busca_cep(cep)

            if "erro" not in response:
                endereco = {
                    "cep": response.get("cep", ""),
                    "logradouro": response.get("logradouro", ""),
                    "complemento": response.get("complemento", ""),
                    "bairro": response.get("bairro", ""),
                    "cidade": response.get("localidade", ""),
                    "uf": response.get("uf", "")
                }
                return endereco
            else:
                print("CEP não encontrado. Tente novamente.")
        else:
            print("CEP inválido. Digite um valor válido com 8 dígitos.")