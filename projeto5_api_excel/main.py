# Criação de um ETL para consumir dados de uma API e salvar em um arquivo Excel

# ==================================================
# ETL - EXTRACT
# ==================================================

# requests = conversar com APIs
import requests


# ==================================================
# URL DA API
# ==================================================

url = "https://jsonplaceholder.typicode.com/users"

# ==================================================
# REQUISIÇÃO
# ==================================================
print("\n-----------------------------------")
print("Enviando requisição para API...")
print("-----------------------------------\n")
resposta = requests.get(url)

# ==================================================
# STATUS HTTP
# ==================================================
print("-----------------------------------")
print("Status da resposta:")
print("-----------------------------------\n")
print(resposta.status_code)

print("200 é Código HTTP.\n")
print("Requisição bem-sucedida!\n")

# ==================================================
# MOSTRAR RESPOSTA BRUTA
# ==================================================
print("\nRESPOSTA DA API:\n")

print("\n================ RESPOSTA BRUTA ================\n")
print(resposta.text)
print("\n================ RESPOSTA BRUTA ================\n")


# ==================================================
# ETL - TRANSFORM
# ==================================================

# ==================================================
# TRANSFORMAR JSON EM PYTHON
# ==================================================

dados = resposta.json()

# ==================================================
# TESTE DE DADOS
# ==================================================

print("\n================ TESTE DE DADOS ================\n")

# ==================================================
# TIPO DOS DADOS
# ==================================================
print("---------TIPO DOS DADOS------------")
print("Tipo da variável dados:")
print(type(dados))
print("-----------------------------------")

# ==================================================
# PRIMEIRO USUÁRIO
# ==================================================
print("------------PRIMEIRO USUÁRIO------------")
print("Primeiro usuário:")
print(dados[0])
print("-----------------------------------------")

# ==================================================
# DADOS ESPECÍFICOS
# ==================================================
print("-------------DADOS ESPECÍFICOS------------")
usuario = dados[0]
print("Nome:")
print(usuario["name"])
print("\nEmail:")
print(usuario["email"])
print("-------------------------------------------")

print("================ TESTE DE DADOS ================\n")

# ==================================================
# LOOP USUÁRIOS
# ==================================================
print("\n================ USUÁRIOS ================\n")
for usuario in dados:
    print(usuario["name"])

# ==================================================
# ETL - LOAD
# ==================================================

# openpyxl = biblioteca para Excel
from openpyxl import Workbook

# ==================================================
# CRIAR EXCEL
# ==================================================
print("================ PLANILHA ================\n")

print("Criando arquivo Excel...\n")
# cria workbook Excel
workbook = Workbook()
# pega planilha ativa
planilha = workbook.active
# nome da aba
planilha.title = "Usuarios"

# ==================================================
# CABEÇALHO
# ==================================================
print("Criando cabeçalho...\n")
planilha.append([
    "Nome",
    "Email",
    "Cidade",
    "Site"
])

# ==================================================
# ADICIONAR DADOS
# ==================================================

print("Adicionando dados...\n")
for usuario in dados:

    nome = usuario["name"]

    email = usuario["email"]

    cidade = usuario["address"]["city"]

    site = usuario["website"]

    # adiciona linha no Excel
    planilha.append([
        nome,
        email,
        cidade,
        site
    ])



# ==================================================
# CRIAR PASTA DE RELATÓRIOS
# ==================================================
import os

pasta_relatorios = "/Users/cffadv/Python-rpa/projeto5_api_excel/relatorios"
os.makedirs(pasta_relatorios, exist_ok=True)

# ==================================================
# CAMINHO DO EXCEL
# ==================================================

caminho_arquivo = os.path.join(
    pasta_relatorios,
    "usuarios.xlsx"
)
# ==================================================
# PADRONIZAR NOME DO ARQUIVO EXCEL
# ==================================================

from datetime import datetime
# biblioteca para data e hora

data_atual = datetime.now().strftime("%Y-%m-%d")


# ==================================================
# SALVAR EXCEL
# ==================================================
caminho_arquivo = f"/Users/cffadv/Python-rpa/projeto5_api_excel/relatorios/usuarios_{data_atual}.xlsx"

workbook.save(caminho_arquivo)
print("Excel criado com sucesso!\n")
print(f"Arquivo salvo: {caminho_arquivo}")




print("================ PLANILHA ================\n")