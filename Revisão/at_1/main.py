import flet as ft #ft é uma abreviação para facilitar a chamada

def main(page): #tudo abaixo daqui é fará parte de uma página

    def botao_clicar(e): #função executar botão
        page.add(ft.Text("Olá Mundo"))
        page.update()

    cor_options = [ #opções para o dropdown
        ft.dropdown.Option("Laranja"),
        ft.dropdown.Option("Vermelho"),
        ft.dropdown.Option("Azul"),
        ft.dropdown.Option("Nenhuma acima") 
    ]

    tx_titulo = ft.Text("Aqui uma leve demonstração dos componentes do Flet", size = 20)
    bt_clique = ft.ElevatedButton(text = "Clique", on_click=botao_clicar)
    tf_corFavorita = ft.TextField(label="Qual a sua cor favorita? ")
    cb_pergunta = ft.Checkbox(label="Está certo de sua resposta?")
    dd_corFavorita = ft.Dropdown("Sua cor é uma delas?", options=cor_options)
    ad_alerta = ft.AlertDialog(
        title = ft.Text("Confirmação"),
        content = ft.Text("Tem certesa MESMO que sua cor é essa (pergunta eliminatória)"),
        actions = [
            ft.TextButton("Sim"),
            ft.TextButton("Não")
        ] 
    )

    page.add(tx_titulo, #adiciona os componentes à tela
             bt_clique,
             tf_corFavorita,
             dd_corFavorita,
             cb_pergunta,
             ad_alerta,
             
             )
    
ft.app(target=main)