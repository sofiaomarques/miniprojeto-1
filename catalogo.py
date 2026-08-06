import json
from collections import deque
class Catalogo:
    def __init__(self, caminho_json: str):
        with open(caminho_json, encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        self.plataforma=dados["plataforma"]
        self.meta=dados["meta"]
        self.conteudos=dados["conteudos"]
        self.usuarios=dados["usuarios"]
    def mostrar (self):
        print(self.dados)
cat1= Catalogo("/catalogo_dev.json")
cat1.mostrar()
