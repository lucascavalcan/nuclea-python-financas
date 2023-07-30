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
                    "CEP": response.get("cep"),
                    "Logradouro": response.get("logradouro"),
                    "Complemento": response.get("complemento"),
                    "Bairro": response.get("bairro"),
                    "Cidade": response.get("localidade"),
                    "Estado": response.get("uf")
                }
                return endereco
            else:
                print("CEP não encontrado. Tente novamente.")
        else:
            print("CEP inválido. Digite um valor válido com 8 dígitos.")