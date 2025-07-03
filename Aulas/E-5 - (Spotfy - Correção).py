import flet as ft

def main(tela: ft.Page):
    tela.theme_mode=ft.ThemeMode.DARK
    tela.title="Spotfy Senac"
    tela.scroll=ft.ScrollMode.AUTO
    
    album = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.ALBUM),
                        title=ft.Text("O Rappa"),
                        subtitle=ft.Text("Pescador de Ilusões")
                    ),
                    ft.Row(
                        [
                          ft.TextButton("Add Play List"), 
                          ft.TextButton("Play")
                        ],
                        alignment=ft.MainAxisAlignment.END
                    )
                ]
            ),
            width=400,padding=5
        )
    )
    
    
    layout = ft.Row(
        controls=[
           ft.Column(
               [
                    ft.Text("Spotfy Senac MS", weight="bold", size=32 ),
                    album,album,album,album,album
               ]
            ),
           ft.Column(
               [
                   ft.Container(
                       content=ft.Icon(ft.icons.PLAY_CIRCLE_OUTLINE_SHARP, color="green", size=150),
                       width=400,
                       height=400,
                       bgcolor=ft.colors.BLACK26,
                       border_radius=10
                   ),
                   ft.Text("Capital Inícial", weight="bold",size=30, width="400", text_align="center"),
                   ft.Text("Natasha",width="400", text_align="center"),
                   ft.Row([
                       ft.Icon(ft.icons.SKIP_PREVIOUS,color="green", size=50),
                       ft.Icon(ft.icons.PLAY_ARROW,color="green", size=50),
                       ft.Icon(ft.icons.SKIP_NEXT,color="green", size=50)
                   ],alignment=ft.MainAxisAlignment.CENTER, width=400)
               ]
           )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    tela.add(layout)
ft.app(main)