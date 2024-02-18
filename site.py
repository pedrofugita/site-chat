# botão de iniciar chat
# pop-up para entrar no chat
# quando entrar no chat
    # mensagem que você entrou (aparece para todos)
    # campo e botão para enviar mensagem
# cada mensagem que você envia (aparece para todos)
    # Nome: Texto da mensagem

# frontend é o que o usuário vê
# backend lógica para rodar o site

# django, flask, react -> frameworks para criação de sites

# produto = {
#     "nome": "iphone",
#     "preço": 6500,
#     "quantidade": 150
# }
#
# produto["quantidade"]

import flet as ft

def main(pagina):
    texto = ft.Text("CHAT PARA XINGAR O CARLITO", size=72, color=ft.colors.BLUE)

    chat = ft.Column()

    nome_usuario = ft.TextField(label="Escreva seu nome")

    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem["tipo"]
        if tipo == "mensagem":
            texto_mensagem = mensagem["texto"]
            usuario_mensagem = mensagem ["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensagem}"))     # adiciona a mensagem no chat
        else:
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem} entrou no chat",
                                         size=12, italic=True, color=ft.colors.RED))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)   # publish-subscribe (PUBSUB) canal de comunicação

    def enviar_mensagem(evento):
        pagina.pubsub.send_all({"texto": campo_mensagem.value, "usuario": nome_usuario.value, "tipo": "mensagem"})  # define um dicionário
        campo_mensagem.value = ""  # limpa o campo de mensagem
        pagina.update()



    campo_mensagem = ft.TextField(label="Digite sua mensagem")
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)


    def entrar_popup (evento):
        pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})
        pagina.add(chat)
        popup.open=False    # fechar popup
        pagina.update()     # atualiza pagina a cada ação
        pagina.remove(botao_iniciar)    # remove o botão iniciar
        pagina.remove(texto)    # remove título do site
        pagina.add(ft.Row([campo_mensagem, botao_enviar]))      # cria campo de mensagem e botão de enviar em linha
        pagina.update()



    popup = ft.AlertDialog(
        open=False, # quando abrir estará fechado
        modal=True, # pop-up = modal
        title=ft.Text("Bem vindo!"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_popup)]
        )

    def entrar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        #texto_entrou = ft.Text("Entrou no chat")
        #pagina.add(texto_entrou)


    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=entrar_chat)
    #botao_iniciar2 = ft.TextButton("Iniciar chat")

    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main, view=ft.WEB_BROWSER, port=8000) # WEB_BROWSER para site
