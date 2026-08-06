# Mini-Projeto TrilhaSonora

Este projeto implementa um analisador do catálogo da TrilhaSonora usando apenas Python e a biblioteca padrão.

## Escolhas

A classe `Catalogo` traz a leitura, a limpeza e as consultas ao catálogo porque todos os métodos obrigatórios dependem dos mesmos dados carregados do JSON. Assim, o arquivo é lido uma única vez no `__init__`.

Usei `conteudos_por_id` para acessar conteúdos diretamente pelo id, sem percorrer a lista completa a toda consulta.

Usei `conteudos_por_genero` para guardar os ids por gênero já no carregamento do catálogo. Isso torna `conteudos_do_genero` mais simples e rápido.

Usei `deque` para a fila de reprodução porque a fila precisa inserir no final e remover do início em ordem FIFO.

As limpezas dos dados acontecem no `__init__`: ratings são convertidos para `float`, datas são padronizadas em `YYYY-MM-DD`, gêneros são transformados em listas simples ordenadas e execuções são convertidas para `int`. (Com base nos 7 problemas dados no readme inicial).

No `main.py`, usei `getattr` para chamar o método indicado em cada consulta sem precisar escrever uma sequência grande de `if` e `elif`.

O `cli.py` oferece um menu interativo no terminal para listar usuários, consultar playlists, buscar dados de conteúdos, pesquisar por gênero e controlar a fila de reprodução.

## Como rodar

Para gerar o arquivo de respostas:

```bash
python3 main.py
```

Para abrir o menu interativo:

```bash
python3 cli.py
```

Para testar a classe diretamente:

```bash
python3 catalogo.py
```

O arquivo gerado pela execução principal é `respostas.json`.
