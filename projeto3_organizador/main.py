# OS = manipula sistemas operacionais, arquivos, pastas, etc
import os   
# shutil = move um arquivo de um lugar para outro
import shutil

# nome da pasta onde estão os arquivos
pasta_origem = "/Users/cffadv/Python-rpa/projeto3_organizador/arquivos"


# lista arquivos da pasta
arquivos = os.listdir(pasta_origem)


# preciso de um loop para ler cada arquivo da pasta
for arquivo in arquivos:
    # definir o caminho completo do arquivo
    caminho_arquivo = os.path.join(pasta_origem, arquivo)
    
    ##agora preciso verificar se é de fato um arquivo, e nao uma pasta
    if os.path.isfile(caminho_arquivo):

        # -------------------------------
        # ORGANIZAR IMAGENS
        # -------------------------------

        # verificar se o arquivo é uma imagem (jpg, png, jpeg)
        if arquivo.endswith(".jpg") or arquivo.endswith(".png") or arquivo.endswith(".jpeg"):
            # definir a pasta de destino para imagens
            pasta_destino = os.path.join(pasta_origem, "imagens")
            # criar a pasta de destino se nao existir
            os.makedirs(pasta_destino, exist_ok=True)
            # mover o arquivo para a pasta de destino
            shutil.move(caminho_arquivo, os.path.join(pasta_destino, arquivo))
            # apos realizar tudo isso mostra no terminal a imagem movida para pasta
            print("\n================ IMAGENS ================")
            print(f"{arquivo}  movido para --> {pasta_destino}")


        # -------------------------------
        # ORGANIZAR PDF
        # -------------------------------

        # verificar se o arquivo é um PDF
        elif arquivo.endswith(".pdf"):
            # definir a pasta de destino para PDF
            pasta_destino = os.path.join(pasta_origem, "pdfs")
            # criar a pasta de destino se nao existir
            os.makedirs(pasta_destino, exist_ok=True)
            # mover o arquivo para a pasta de destino
            shutil.move(caminho_arquivo, os.path.join(pasta_destino, arquivo))
            # apos realizar tudo isso mostra no terminal o PDF movido para pasta
            print("\n================ PDF ================")
            print(f"{arquivo}  movido para --> {pasta_destino}")

        # -------------------------------
        # ORGANIZAR PLANILHAS
        # -------------------------------
        # verificar se o arquivo é uma planilha (xlsx, csv)
        elif arquivo.endswith(".xlsx") or arquivo.endswith(".csv"):
            # definir a pasta de destino para planilhas
            pasta_destino = os.path.join(pasta_origem, "planilhas")
            # criar a pasta de destino se nao existir
            os.makedirs(pasta_destino, exist_ok=True)
            # mover o arquivo para a pasta de destino
            shutil.move(caminho_arquivo, os.path.join(pasta_destino, arquivo))
            # apos realizar tudo isso mostra no terminal a planilha movida para pasta
            print("\n================ PLANILHAS ================")
            print(f"{arquivo}  movido para --> {pasta_destino}")

        # -------------------------------
        # OUTROS ARQUIVOS
        # -------------------------------
        # se o arquivo nao for nenhum dos tipos anteriores, move para pasta "outros"
        else:
            pasta_destino = os.path.join(pasta_origem, "outros")
            os.makedirs(pasta_destino, exist_ok=True)
            shutil.move(caminho_arquivo, os.path.join(pasta_destino, arquivo))
            print("\n================ OUTROS ================")
            print(f"{arquivo}  movido para --> {pasta_destino}")

