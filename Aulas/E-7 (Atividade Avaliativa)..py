import flet as ft
def main(pg:ft.Page):
    pg.spacing=15
    pg.padding=18
    pg.theme_mode=ft.ThemeMode.DARK
    pg.auto_scroll=ft.ScrollMode.AUTO

    barra_menu = ft.AppBar(
        leading=ft.IconButton(ft.icons.EDIT_NOTE, icon_color='Black', on_click=lambda e: pg.open(drawer_menu)),
        leading_width=40,
        title=ft.Text("CGP (Cadastro e Gerenciamento de Produtos)",color=ft.colors.BLUE_700, weight='bold'),
        bgcolor="#92FFC0"
    )        

    listaProdutos=[]

    def salvar_dados(e):
        produto = {
            "Nome":tf_nome.value,
            "Categoria":tf_categoria.value,
            "Preço":tf_preco.value,
            "Quantidade Disponível":tf_qtd.value
        }
        listaProdutos.append(produto)

        listaDtRow=[]
        for produto in listaProdutos:
            listaDtRow.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(produto["Nome"])),
                        ft.DataCell(ft.Text(produto["Categoria"])),
                        ft.DataCell(ft.Text(produto["Preço"])),
                        ft.DataCell(ft.Text(produto["Quantidade Disponível"])),
                    ]
                )
            )
        tb_produtos.rows=listaDtRow

        tf_nome=None
        tf_categoria=None
        tf_preco=None
        tf_qtd=None   

    def acao_drawer(e):
        match (drawer_menu.selected_index+1):
            case 1:
                pg.go("/pagina1")
            case 2:
                pg.go("/pagina2")
            case 3:
                pg.go("/pagina3")

    drawer_menu = ft.NavigationDrawer(
        on_change=acao_drawer,
        controls=[
            ft.NavigationDrawerDestination(label="Página Principal",
                                           icon=ft.icons.HOME),
            ft.NavigationDrawerDestination(label="Registrar Produto",
                                           icon=ft.icons.POST_ADD),
            ft.NavigationDrawerDestination(label="Visualizar Produtos Registrados",
                                           icon=ft.icons.SHOPPING_BAG)
        ]
    )

    def navegacao(route):
        pg.views.clear()

        if pg.route == "/pagina1":
            pg.views.append(paginaHome)
        if pg.route == "/pagina2":
            pg.views.append(paginaPro)
        if pg.route == "/pagina3":
            pg.views.append(paginaView)
        pg.update()

    paginaHome = ft.View(
        route="/pagina1",
        appbar=barra_menu,
        drawer=drawer_menu,
        controls=[
            ft.Text("Página Principal", style="headlineMedium"),
            ft.Text("Caso queira, você pode cadastrar um produto ou simplesmente visualizar os já cadastrados"),
        ]
    )


    tf_nome = ft.TextField(label="Nome", bgcolor="darkgray", width=300)
    tf_categoria = ft.TextField(label="Categoria", bgcolor="darkgray", width=300)
    tf_preco = ft.TextField(label="Preço", bgcolor="darkgray", width=300)
    tf_qtd= ft.TextField(label="Quantidade em estoque", bgcolor="darkgray", width=300)
    bt_salvar = ft.ElevatedButton(text="Salvar",bgcolor="darkgray", on_click= salvar_dados)

    paginaPro = ft.View(
        route="/pagina2",
        appbar=barra_menu,
        drawer=drawer_menu,
        controls=[
            ft.Text("Cadastro de Produtos", style="headlineMedium"),
            ft.Text("Registre os produtos no sistema à vontade"),
            tf_nome,
            tf_categoria,
            tf_preco,
            tf_qtd,
            bt_salvar
        ]
    )


    tb_produtos = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Nome")),
            ft.DataColumn(ft.Text("E-mail")),
            ft.DataColumn(ft.Text("Telefone"))
        ],
        rows=[]
    )

    paginaView = ft.View(
        route="/pagina3",
        appbar=barra_menu,
        drawer=drawer_menu,
        controls=[
            ft.Text("Produtos Cadastrados", style="headlineMedium"),
            ft.Text("Todos os produtos já cadastrados são mostrados aqui"),
            tb_produtos
        ]
    )

    pg.add()

    pg.on_route_change=navegacao
    pg.go('/pagina1')

ft.app(main)