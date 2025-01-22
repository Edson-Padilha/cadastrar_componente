import pyautogui as pag
from time import sleep

cache_imagens = {}

# Função para procurar imagens obrigatórias
def localizar_imagem(caminho_imagem, confidence=0.9):
    if caminho_imagem not in cache_imagens:
        while True:
            try:
                localizacao = pag.locateOnScreen(caminho_imagem, confidence=confidence)

                if localizacao is not None:
                    print(f"Imagem {caminho_imagem} encontrada!")
                    cache_imagens[caminho_imagem] = localizacao
                    break

                else:
                    print(f"Imagem {caminho_imagem} não encontrada. Tentando naovamente...")
                    sleep(1)

            except pag.ImageNotFoundException:
                print(f"Imagem {caminho_imagem} não encontrada. Tentando novamente...")
                sleep(1)
    
    return cache_imagens[caminho_imagem]