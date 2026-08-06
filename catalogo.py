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
        self.conteudos_por_id = {}
        self.conteudos_por_genero = {}
        self.fila = deque()
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

            execucoes = n.get("engajamento", {}).get("execucoes")
            if type(execucoes) == str:
                if "," in execucoes:
                    execucoes = execucoes.split(",")
                    saida = ""
                    for i in execucoes:
                        saida += i
                    n["engajamento"]["execucoes"] = int(saida)
                else:
                    n["engajamento"]["execucoes"] = int(n["engajamento"]["execucoes"])

            self.conteudos_por_id[n["id"]] = n
            for genero in n["generos"]:
                if genero not in self.conteudos_por_genero:
                    self.conteudos_por_genero[genero] = []
                self.conteudos_por_genero[genero].append(n["id"])

    def listar_usuarios(self) -> list[str]:
        nomes = []
        for usuario in self.usuarios:
            nomes.append(usuario["nome"])
        return sorted(nomes)
    def buscar_usuario_por_nome(self, nome: str) -> str | None:
        nome_procurado = nome.lower()
        for usuario in self.usuarios:
            if usuario["nome"].lower() == nome_procurado:
                return usuario["id"]
        return None
    def playlist_de(self, usuario_id: str) -> list[str] | None:
        for usuario in self.usuarios:
            if usuario["id"] == usuario_id:
                return usuario["playlist"]
        return None

    def conteudo_na_posicao(self, usuario_id: str, posicao: int) -> str | None:
        playlist = self.playlist_de(usuario_id)
        if playlist is None:
            return None
        if posicao < 0 or posicao >= len(playlist):
            return None
        return playlist[posicao]

    def intersecao_playlists(self, usuario_ids: list[str]) -> list[str]:
        playlists = []
        for usuario_id in usuario_ids:
            playlist = self.playlist_de(usuario_id)
            if playlist is None:
                return []
            playlists.append(set(playlist))

        if len(playlists) == 0:
            return []

        conteudos_em_comum = playlists[0]
        for playlist in playlists[1:]:
            conteudos_em_comum = conteudos_em_comum.intersection(playlist)
        return sorted(conteudos_em_comum)

    
    def rating_de(self, conteudo_id: str) -> float | None:
        conteudo = self.conteudos_por_id.get(conteudo_id)
        if conteudo is None:
            return None
        return conteudo["rating"]

    def duracao_total_de(self, conteudo_id: str) -> int | None:
        conteudo = self.conteudos_por_id.get(conteudo_id)
        if conteudo is None:
            return None

        if conteudo["tipo"] == "musica":
            return conteudo["duracao_seg"]

        duracao_total = 0
        for faixa in conteudo["faixas"]:
            if faixa["duracao_seg"] is not None:
                duracao_total += faixa["duracao_seg"]
        return duracao_total

    def generos_de(self, conteudo_id: str) -> list[str] | None:
        conteudo = self.conteudos_por_id.get(conteudo_id)
        if conteudo is None:
            return None
        return conteudo["generos"]

    def plataformas_de(self, conteudo_id: str) -> list[str] | None:
        conteudo = self.conteudos_por_id.get(conteudo_id)
        if conteudo is None:
            return None
        return sorted(conteudo.get("plataformas", []))

    def data_adicionado_de(self, conteudo_id: str) -> str | None:
        conteudo = self.conteudos_por_id.get(conteudo_id)
        if conteudo is None:
            return None
        return conteudo["data_adicionado"]

    def execucoes_de(self, conteudo_id: str) -> int | None:
        conteudo = self.conteudos_por_id.get(conteudo_id)
        if conteudo is None:
            return None
        if "engajamento" not in conteudo:
            return None
        return conteudo["engajamento"]["execucoes"]

    def conteudos_do_genero(self, genero: str) -> list[str]:
        return sorted(self.conteudos_por_genero.get(genero, []))

 
    def enfileirar(self, conteudo_id: str) -> bool:
        if conteudo_id not in self.conteudos_por_id:
            return False
        self.fila.append(conteudo_id)
        return True

    def proximo(self) -> str | None:
        if len(self.fila) == 0:
            return None
        return self.fila.popleft()

    def fila_atual(self) -> list[str]:
        return list(self.fila)

    def mostrar (self):
        print(self.conteudos)
cat1= Catalogo("catalogo_dev.json")
cat1.mostrar()
