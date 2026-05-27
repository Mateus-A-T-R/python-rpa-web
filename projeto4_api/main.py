# ==========================================
# IMPORTAR BIBLIOTECA
# ==========================================

import requests


# ==========================================
# URL DA API
# ==========================================

url = "https://jsonplaceholder.typicode.com/users"


# ==========================================
# FAZER REQUISIÇÃO PARA API
# ==========================================

print("Enviando pedido para API...\n")

resposta = requests.get(url)

print("Resposta recebida!\n")


# ==========================================
# VER STATUS DA RESPOSTA
# ==========================================

print("Status HTTP:")
print(resposta.status_code)

# 200 = sucesso


# ==========================================
# MOSTRAR TEXTO BRUTO DA API
# ==========================================

print("\nResposta original da API:\n")

print(resposta.text)


# ==========================================
# CONVERTER JSON PARA PYTHON
# ==========================================

dados = resposta.json()


# ==========================================
# MOSTRAR DADOS ORGANIZADOS
# ==========================================

print("\n================ USUÁRIOS ================\n")


for usuario in dados:

    print(f"Nome: {usuario['name']}")

    print(f"Email: {usuario['email']}")

    print(f"Cidade: {usuario['address']['city']}")

    print("\n-----------------------------------")