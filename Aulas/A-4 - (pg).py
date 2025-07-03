import flet as ft
import flet.canvas as cv
def main (pg: ft.Page):
    pg.title="AAAAAAAAAAAAAAAAAAAAAA"
    pg.theme_mode=ft.ThemeMode.DARK
    pg.window_width=1200
    pg.window_height=1000
    pg.scroll=ft.ScrollMode.AUTO

    #alerta de diálogo
    def alerta(e):
        dialog=ft.AlertDialog(title=ft.Text("Atenção!"),content=ft.Text("Você Clicou no float button!"),
)
        pg.dialog=dialog
        dialog.open=True
        pg.update()

    tx_texto = ft.Text("Elementos de Layout com Flet", size=20)

    #imagem site
    img_imagem1 = ft.Image(src="https://img.gamewith.net/article/thumbnail/rectangle/10058.png",
                           width=500)
    
    #imagem pasta
    img_imagem2 = ft.Image(src="src/rathian.png",
                          width=600)
    
    #icone
    ic_icone = ft.Icon(name="add",color="purple",size=100)

    #botão flutuante
    bt_float = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=alerta)

    #ListView
    ls_lista=ft.ListView(
        expand=True,
        spacing=10,
        padding=10,
        auto_scroll=True,
        controls=[
            ft.Text("Contato 1"),
            ft.Text("Contato 2"),
            ft.Text("Contato 3"),
            ft.Text("Contato 4"),
            ft.Text("Contato 5"),
            ft.Text("Contato 6"),
            ft.Text("Contato 7"),
        ]
    )
    tb_tabela = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Nome",color="green")),
            ft.DataColumn(ft.Text("E-mail",color="green")),
            ft.DataColumn(ft.Text("Telefone",color="green"))
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Joao Dev")),
                    ft.DataCell(ft.Text("joaodev123@gmail.com")),
                    ft.DataCell(ft.Text("(+55)67 99999-9999"))
                ]
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Davi")),
                    ft.DataCell(ft.Text("meurerdavi569@gmail.com")),
                    ft.DataCell(ft.Text("(+55)67 99226-9268"))
                ]
            )
        ]
    )
    a1 = ft.CircleAvatar(
        foreground_image_src="https://avatars.githubusercontent.com/u/5041459?s=88&v=4",
        content=ft.Text("FF"),
    )

    loading = ft.CupertinoActivityIndicator(
            radius=50,
            color=ft.colors.RED,
            animating=True,
           )
    
    lista_icone = ft.Row(
        [
            ft.Icon(name=ft.icons.FAVORITE,color=ft.colors.PINK),
            ft.Icon(name=ft.icons.AUDIOTRACK,color=ft.colors.GREEN_400,size=30),
            ft.Icon(name=ft.icons.BEACH_ACCESS,color=ft.colors.BLUE,size=50),
            ft.Icon(name="settings",color="c1c1c1")
        ]
    )

    pg.add(tx_texto,
           img_imagem1,
           img_imagem2,
           ic_icone,
           bt_float,
           ls_lista,
           tb_tabela,
           a1,
           loading,
           lista_icone)

ft.app(main)