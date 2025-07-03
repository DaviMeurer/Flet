import flet as ft

def main(page):
    page.title = "Exemplo de Layout completo"

    conteudo = ft.Column(
        controls = [
            ft.Text("Formulário de cadastro", size = 24),
            ft.TextField(label="Nome: "),
            ft.TextField(label = "E-mail: "),

            ft.Row(
                controls = [
                    ft.ElevatedButton("Enviar", on_click = lambda e: print("CU PRETO")),
                    ft.ElevatedButton("Cancelar")
                ],
                spacing = 15,
                alignment = ft.alignment.center,
            )
        ],
        spacing = 15,
        alignment = ft.alignment.center,
        horizontal_alignment = ft.CrossAxisAlignment.START,
    )

    page.add(conteudo)

ft.app(target=main)