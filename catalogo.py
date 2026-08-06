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
        for n in self.conteudos:
            if "rating" in n:
                if type(n["rating"]) == str or type(n["rating"]) == int:
                    n["rating"] = float(n["rating"])
            else:
                n["rating"] = None 

            data = n["data_adicionado"]
            if "/" in data:
                data = data.split("/")
                n["data_adicionado"] = f"{data[2]}-{data[1]}-{data[0]}"
            if type(n["generos"]) == str:
                n["generos"] = [n["generos"]]
            pilha = [n["generos"]]
            resultado = []
            while len(pilha) > 0:
                atual = pilha[-1]
                if type(atual) == list:
                     for c in pilha.pop():
                         pilha.append(c)
                else:
                    resultado.append(atual)
                    pilha.pop()
            resultado.sort()
            n["generos"] = resultado

            execucoes = n["engajamento"]["execucoes"]
            if type(execucoes) == str:
                if "," in execucoes:
                    execucoes = execucoes.split(",")
                    


    def mostrar (self):
        print(self.conteudos)
cat1= Catalogo("catalogo_dev.json")
cat1.mostrar()
