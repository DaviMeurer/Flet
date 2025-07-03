import flet as ft

def main(tela: ft.Page):
    tela.title="Orientação de Layout"
    tela.theme_mode=ft.ThemeMode.DARK
    tela.scroll=ft.ScrollMode.AUTO
    tela.padding=10
    tela.spacing=10

    container = ft.Container(
        content=ft.Icon(ft.icons.ALBUM, color="white"),
        margin=10,
        padding=10,
        alignment=ft.alignment.center,
        bgcolor=ft.colors.GREEN_500,
        width=70,
        height=70,
        border_radius=10,
        on_click=lambda e: print("Cliquei"),
        on_hover=lambda e: print("Passei em cima"),
    )

    coluna = ft.Column(
        [container, container, container],
        alignment=ft.MainAxisAlignment.END
    )
    linha = ft.Row(
        [container, container, container],
        alignment=ft.MainAxisAlignment.CENTER
    )

    album = ft.Container(
        content=ft.Row(
            [
                ft.Icon(ft.icons.ALBUM, color="red", size=40),
                ft.Column(
                    [
                        ft.Text("CPM22", weight="bold", color="black"),
                        ft.Text("Regina Let's GO", color='black')
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ]
        ),
        padding=10,
        alignment=ft.alignment.center,
        bgcolor=ft.colors.GREEN_200,
        width=200,
        height=150,
        border_radius=10
    )

    imagens = []
    for i in range(50):
        imagens.append(
            ft.Image(
                src=f"https://picsum.photos/150/150?{i}",
            )
        )
    grid = ft.GridView(
        controls=imagens,
        expand=0, #ocupa todo o espaço da tela
        runs_count=3, #numero de colunas
        spacing=5,
        run_spacing=10, #espaçamento vertical
        max_extent=100
    )

    tela.add(coluna,
             linha,
             album,
             grid)

ft.app(target=main)
