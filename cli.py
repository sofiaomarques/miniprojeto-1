import catalogo


cat1 = catalogo.Catalogo("catalogo_final.json")


def mostrar_menu():
    print()
    print("TrilhaSonora")
    print("============")
    print("1. Listar todos os usuários")
    print("2. Ver playlist completa de um usuário")
    print("3. Conteúdo na posição N da playlist")
    print("4. Interseção de playlists")
    print("5. Dados de um conteúdo")
    print("6. Conteúdos de um gênero")
    print("7. Enfileirar conteúdo na fila de reprodução")
    print("8. Tocar próximo da fila")
    print("9. Ver fila atual")
    print("0. Sair")


def mostrar_lista(lista):
    if len(lista) == 0:
        print("Nenhum resultado.")
    else:
        for item in lista:
            print(item)


def descricao_conteudo(conteudo_id):
    conteudo = cat1.conteudos_por_id.get(conteudo_id)
    if conteudo is None:
        return conteudo_id
    return f'{conteudo["titulo"]}, de {conteudo["artista"]} ({conteudo["tipo"]}) - {conteudo_id}'


def mostrar_conteudos(conteudo_ids):
    if len(conteudo_ids) == 0:
        print("Nenhum resultado.")
    else:
        for posicao, conteudo_id in enumerate(conteudo_ids, 1):
            print(f"{posicao}. {descricao_conteudo(conteudo_id)}")


def mostrar_playlist(usuario_id):
    playlist = cat1.playlist_de(usuario_id)
    if playlist is None:
        print("Usuário não encontrado.")
    else:
        mostrar_conteudos(playlist)


opcao = ""

while opcao != "0" and opcao != "10":
    mostrar_menu()
    opcao = input("> ")

    if opcao == "1":
        usuarios = cat1.listar_usuarios()
        mostrar_lista(usuarios)

    elif opcao == "2":
        nome = input("Nome do usuário: ")
        usuario_id = cat1.buscar_usuario_por_nome(nome)
        if usuario_id is None:
            print("Usuário não encontrado.")
        else:
            mostrar_playlist(usuario_id)

    elif opcao == "3":
        nome = input("Nome do usuário: ")
        usuario_id = cat1.buscar_usuario_por_nome(nome)
        if usuario_id is None:
            print("Usuário não encontrado.")
        else:
            playlist = cat1.playlist_de(usuario_id)
            print(f"Playlist tem {len(playlist)} itens.")
            texto_posicao = input("Posição: ")
            if texto_posicao.isdigit():
                posicao = int(texto_posicao) - 1
                conteudo_id = cat1.conteudo_na_posicao(usuario_id, posicao)
                if conteudo_id is None:
                    print("Posição inválida.")
                else:
                    print(descricao_conteudo(conteudo_id))
            else:
                print("Posição inválida.")

    elif opcao == "4":
        nomes = input("Nomes dos usuários separados por vírgula: ")
        usuario_ids = []
        algum_invalido = False

        for nome in nomes.split(","):
            usuario_id = cat1.buscar_usuario_por_nome(nome.strip())
            if usuario_id is None:
                algum_invalido = True
            else:
                usuario_ids.append(usuario_id)

        if algum_invalido:
            print("Algum usuário não foi encontrado.")
        else:
            resultado = cat1.intersecao_playlists(usuario_ids)
            mostrar_conteudos(resultado)

    elif opcao == "5":
        conteudo_id = input("Id do conteúdo: ")
        rating = cat1.rating_de(conteudo_id)

        if rating is None and cat1.generos_de(conteudo_id) is None:
            print("Conteúdo não encontrado.")
        else:
            print(f"Conteúdo: {descricao_conteudo(conteudo_id)}")
            print(f"Rating: {rating}")
            print(f"Duração: {cat1.duracao_total_de(conteudo_id)}")
            print(f"Gêneros: {cat1.generos_de(conteudo_id)}")
            print(f"Plataformas: {cat1.plataformas_de(conteudo_id)}")
            print(f"Data adicionado: {cat1.data_adicionado_de(conteudo_id)}")
            print(f"Execuções: {cat1.execucoes_de(conteudo_id)}")

    elif opcao == "6":
        genero = input("Gênero: ")
        conteudos = cat1.conteudos_do_genero(genero)
        mostrar_conteudos(conteudos)

    elif opcao == "7":
        conteudo_id = input("Id do conteúdo: ")
        if cat1.enfileirar(conteudo_id):
            print("Conteúdo enfileirado.")
        else:
            print("Conteúdo não encontrado.")

    elif opcao == "8":
        proximo = cat1.proximo()
        if proximo is None:
            print("Fila vazia.")
        else:
            print(descricao_conteudo(proximo))

    elif opcao == "9":
        fila = cat1.fila_atual()
        mostrar_conteudos(fila)

    elif opcao == "0" or opcao == "10":
        print("Saindo.")

    else:
        print("Opção inválida.")
