# Sistema de Gestão de Carteira de Ações

Este é um projeto de uma aplicação em Python para a gestão de carteira de ações. A aplicação oferece um menu interativo com diversas opções para o usuário gerenciar suas ações e informações de clientes. O projeto foi desenvolvido como parte do módulo de Python da formação em DevOps fornecida pela [Ada] em parceira com a [Nuclea]. A aplicação possui os seguintes requisitos:

## Funcionalidades

### 1. Cliente:

* CRUD de Clientes
* Campos inclusos no cadastro: Nome, CPF, RG, Data de Nascimento, CEP, Logradouro, Complemento, Bairro, Cidade, Estado e Número de Residência
* Validações de CPF, RG, CEP e Data utilizando a biblioteca `validate-docbr`

### 2. Ordem:

* Cadastro de ordens de compra de ações
* Campos solicitados para cadastro: Nome, Ticket, Valor da Compra, Quantidade de Compra, Data de Compra e CPF do cliente vinculado à ordem
  
### 3. Análise da Carteira:

* Exibição de gráfico com informações das ações cadastradas no banco de dados do cliente
* Determinação da carteira de ações com base no CPF do Cliente utilizando a biblioteca `matplotlib`
  
### 4. Relatórios da Carteira:

* Geração de relatório em formato txt com informações das ações do cliente
* Consulta de dados de ações individuais utilizando a biblioteca `pandas`

### 5. Sair:

* Encerramento da aplicação

## Como Executar o Projeto

1. Clone este repositório para sua máquina local.
2. Certifique-se de ter Python instalado.
3. Instale as dependências necessárias utilizando o gerenciador de pacotes pip:
   
   ```bash
   pip install validate-docbr requests faker psycopg2-binary yfinance matplotlib pandas

4. Navegue até o diretório do projeto e execute o arquivo main.py para iniciar a aplicação.
5. Siga as instruções exibidas no menu para utilizar as funcionalidades da aplicação.

## Autoria

Este projeto foi desenvolvido por [Lucas Cavalcanti de Araujo].