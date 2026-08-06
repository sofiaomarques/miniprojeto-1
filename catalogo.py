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
                    saida = ""
                    for i in execucoes:
                        saida += i
                    n["engajamento"]["execucoes"] = int(saida)
                else:
                    n["engajamento"]["execucoes"] = int(n["engajamento"]["execucoes"])

    def listar_usuarios(self) -> list[str]: ...
    def buscar_usuario_por_nome(self, nome: str) -> str | None: ...
    def playlist_de(self, usuario_id: str) -> list[str] | None: ...
    def conteudo_na_posicao(self, usuario_id: str, posicao: int) -> str | None: ...
    def intersecao_playlists(self, usuario_ids: list[str]) -> list[str]: ...

    
    def rating_de(self, conteudo_id: str) -> float | None: ...
    def duracao_total_de(self, conteudo_id: str) -> int | None: ...
    def generos_de(self, conteudo_id: str) -> list[str] | None: ...
    def plataformas_de(self, conteudo_id: str) -> list[str] | None: ...
    def data_adicionado_de(self, conteudo_id: str) -> str | None: ...
    def execucoes_de(self, conteudo_id: str) -> int | None: ...
    def conteudos_do_genero(self, genero: str) -> list[str]: ...

 
    def enfileirar(self, conteudo_id: str) -> bool: ...
    def proximo(self) -> str | None: ...
    def fila_atual(self) -> list[str]: ...

    def mostrar (self):
        print(self.conteudos)
cat1= Catalogo("catalogo_dev.json")
cat1.mostrar()
