import json
from collections import deque
class Catalogo:
    def __init__(self, caminho_json: str):
        with open(caminho_json, encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        self.conteudos = dados["conteudos"]
        self.usuarios = dados["usuarios"]
        self.conteudos_por_id = {c["id"]: c for c in self.conteudos}
        self.usuarios_por_id = {u["id"]: u for u in self.usuarios}
