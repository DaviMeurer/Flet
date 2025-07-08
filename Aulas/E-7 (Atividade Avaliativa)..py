import flet as ft

def main(pg: ft.Page):

    pg.title = "CGP (Cadastro e Gerenciamento de Produtos)"

    barra_menu = ft.AppBar(
        leading=ft.IconButton(ft.icons.EDIT_NOTE, icon_color='Black', on_click=lambda e: pg.open(drawer_menu)),
        leading_width=40,
    )

    listaProdutos = []

    def valida_nome(e):
        if tf_nome.value=="":
            tf_nome.error_text="Nome incoerente"
        else:
            tf_nome.error_text=None
        pg.update()

    def valida_categoria(e):
        if tf_categoria.value=="":
            tf_categoria.error_text="Categoria inválida"
        else:
            tf_categoria.error_text=None
        pg.update()

    def valida_preco(e):
        if tf_preco.value=="":
            tf_preco.error_text="Insira um preço coerente"
        else:
            tf_preco.error_text=None
        pg.update()

    def valida_quantidade(e):
        if tf_qtd.value=="":
            tf_qtd.error_text="Insira uma quantidade coerente"
        else:
            tf_qtd.error_text=None
        pg.update()
            

    def salvar_dados(e):
        produto = {
            "Nome": tf_nome.value,
            "Categoria": tf_categoria.value,
            "Preço": tf_preco.value,
            "Quantidade Disponível": tf_qtd.value
        }
        listaProdutos.append(produto)

        listaDtRow = []
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
        tb_produtos.rows = listaDtRow
    
    def acao_drawer(e):
        match (drawer_menu.selected_index + 1):
            case 1:
                pg.go("/pagina1")
            case 2:
                pg.go("/pagina2")
            case 3:
                pg.go("/pagina3")

    def acao_drawer(e):
        match (drawer_menu.selected_index + 1):
            case 1:
                pg.go("/pagina1")
            case 2:
                pg.go("/pagina2")
            case 3:
                pg.go("/pagina3")

    drawer_menu = ft.NavigationDrawer(
        on_change=acao_drawer,
        controls=[
            ft.NavigationDrawerDestination(label="Página Principal", icon=ft.icons.HOME),
            ft.NavigationDrawerDestination(label="Registrar Produto", icon=ft.icons.POST_ADD),
            ft.NavigationDrawerDestination(label="Visualizar Produtos Registrados", icon=ft.icons.SHOPPING_BAG),
        ]
    )

    def navegacao(route):
        pg.views.clear()

        if pg.route == "/pagina1":
            pg.views.append(paginaHome)
        elif pg.route == "/pagina2":
            pg.views.append(paginaPro)
        elif pg.route == "/pagina3":
            pg.views.append(paginaView)

        pg.update()  

    paginaHome = ft.View( #Página Principal
        route="/pagina1",
        appbar=barra_menu,
        drawer=drawer_menu,
        controls=[
            ft.AppBar(title=ft.Text("CGP (Cadastro e Gerenciamento de Produtos)", color=ft.colors.BLUE_700, weight='bold'),bgcolor="#92FFC0"),
            ft.Text("Página Principal", style="headlineMedium"),
            ft.Text("Caso queira, você pode cadastrar um produto ou simplesmente visualizar os já cadastrados."),
        ]
    )


    tf_nome = ft.TextField(label="Nome", bgcolor="darkgray", width=300, on_blur=valida_nome)
    tf_categoria = ft.TextField(label="Categoria", bgcolor="darkgray", width=300, on_blur=valida_categoria)
    tf_preco = ft.TextField(label="Preço", bgcolor="darkgray", width=300, on_blur=valida_preco)
    tf_qtd = ft.TextField(label="Quantidade em estoque", bgcolor="darkgray", width=300, on_blur=valida_quantidade)
    bt_salvar = ft.ElevatedButton(text="Salvar", bgcolor="darkgray", on_click=salvar_dados)

    paginaPro = ft.View( #Página de cadastro de produtos
        route="/pagina2",
        appbar=barra_menu,
        drawer=drawer_menu,
        controls=[
            ft.AppBar(title=ft.Text("CGP (Cadastro e Gerenciamento de Produtos)", color=ft.colors.BLUE_700, weight='bold'),bgcolor="#92FFC0"),
            ft.Text("Cadastro de Produtos", style="headlineMedium"),
            ft.Text("Registre os produtos no sistema à vontade"),
            tf_nome,
            tf_categoria,
            tf_preco,
            tf_qtd,
            bt_salvar,
        ]
    )


    tb_produtos = ft.DataTable( 
        columns=[
            ft.DataColumn(ft.Text("Nome")),
            ft.DataColumn(ft.Text("Categoria")),
            ft.DataColumn(ft.Text("Preço")),
            ft.DataColumn(ft.Text("Quantidade Disponível"))
        ]
    )

    paginaView = ft.View( #Página de Visualização de Produtos
        route="/pagina3",
        appbar=barra_menu,
        drawer=drawer_menu,
        controls=[
            ft.AppBar(title=ft.Text("CGP (Cadastro e Gerenciamento de Produtos)", color=ft.colors.BLUE_700, weight='bold'),bgcolor="#92FFC0"),
            ft.Text("Produtos Cadastrados", style="headlineMedium"),
            ft.Text("Todos os produtos já cadastrados são mostrados aqui"),
            tb_produtos
        ]
    )

    pg.on_route_change = navegacao
    pg.go("/pagina1")  

ft.app(main)