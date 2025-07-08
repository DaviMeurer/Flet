import flet as ft

def main(pg=ft.Page):
    pg.title="Spotify Senac (totalmente não é uma cópia do Spotify)"
    pg.auto_scroll=ft.ScrollMode.AUTO
    pg.theme_mode=ft.ThemeMode.DARK

    cardAlbum =  ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text("Faroeste Caboclo"),
                            subtitle=ft.Text(
                                "Que País É Este (1978/1987)', Legião Urbana"
                            ),
                        ),
                        ft.Row(
                            [ft.TextButton("Adicionar à playlist"), ft.TextButton("Escutar")],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        )

    spotify = ft.Card(
        [
            ft.Column(
                [
                 ft.Text("Spotify Senac MS"),
                 cardAlbum,
                 cardAlbum,
                 cardAlbum
                ]
            ),
            ft.Column(
                [
                    ft.Icon(ft.icons.ALBUM_ROUNDED,color="#ffd343"),
                    ft.Text("Rita Lee"),
                    ft.Text("Menina Veneno"),
                    ft.Row(
                        [
                            ft.Icon(name=ft.icons.SKIP_PREVIOUS,color="blue", size=8),
                            ft.Icon(name=ft.icons.PLAY_ARROW, color= "blue"),
                            ft.Icon(name=ft.icons.SKIP_NEXT, color= 'blue', size=8)
                        ]
                    )
                ]
            )
        ]
    )
        
    pg.add(spotify,
           )

ft.app(target=main)