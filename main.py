import json
import catalogo
cat1 = catalogo.Catalogo("catalogo_final.json")

with open("consultas.json", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

respostas = {}

for consulta in dados["consultas"]:
    id_consulta = str(consulta["id"])
    tipo = consulta["tipo"]
    parametros = consulta["parametros"]

    metodo = getattr(cat1, tipo)
    respostas[id_consulta] = metodo(**parametros)

with open("respostas.json", "w", encoding="utf-8") as arquivo:
    json.dump(respostas, arquivo, ensure_ascii=False, indent=2)
