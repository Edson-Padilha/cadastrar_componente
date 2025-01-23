import pyautogui as pag
from time import sleep
from reconhecer_imagem import localizar_imagem
import csv
class CadastrarComponente:
    
    def __init__(self):
        self.pag = pag

    # Carrega as informações do arquivo
    def carregar_dados_csv(arquivo):
        dados = []
        with open(arquivo, 'r') as f:
            leitor_csv = csv.reader(f, delimiter=';')
            next(leitor_csv, None) # Pula o cabeçalho
            
            for linha in leitor_csv:
                if len(linha) >= 2: # Verifica se a linha tem pelo menos duas colunas
                    componente = linha[0]
                    nivel_acesso = linha[1]
                    dados.append((componente, nivel_acesso))
        return dados

# Cria uma instancia da classe 
cadastra = CadastrarComponente()

# Local do arquivo
local_dados = cadastra.carregar_dados_csv()
