import requests

def busca_cep(cep):
    url = f"http://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url).json()
    return response

def valida_cep():
    while True:
        cep = input("Digite o CEP para busca: ")
        response = busca_cep(cep)

        if response:
            endereco = {
                "cep": response["cep"],
                "logradouro": response["logradouro"],
                "complemento": response.get("complemento", ""),
                "bairro": response["bairro"],
                "cidade": response["localidade"],
                "uf": response["uf"]
            }
            return endereco
        else:
            print("CEP não encontrado. Tente novamente.")