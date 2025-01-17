import json
import os

nome_arquivo = "jogos.json"
limpar = "cls"

def limpa(limpar):
    return os.system(limpar)

def lerArquivo() -> list:
    arq = open(nome_arquivo, 'r', encoding='utf-8')
    data = arq.read()
    if len(data) == 0:
        return []
    return json.loads(data)
    
def salvarArquivo(jogos: list):
    arq = open(nome_arquivo, 'w+', encoding='utf-8')
    data = json.dumps(jogos, indent=4)
    arq.write(data)
    arq.close()