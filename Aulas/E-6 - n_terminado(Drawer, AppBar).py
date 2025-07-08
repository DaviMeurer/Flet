import flet as ft
def main(tela: ft.Page):
    tela.theme_mode=ft.ThemeMode.DARK
    tela.auto_scroll=ft.ScrollMode.AUTO
    tela.title('Tela Experimento')

    def drawer_change(e):
        print("Chamei a gaveta")

    def drawer_dismiss(e):
        print(f"Selecionei: {drawer_menu.selected_index}")

    def navegação(route):
        tela.views.clear()
        if tela.route=="/paginaIni":
            tela.views.append(pagina1)
        elif tela.route=='paginaUsu':
            tela.views.append(pagina2)
        elif tela.route=='paginaConfig':
            tela.views.append(pagina3)
        elif tela.route=='paginaConfig':
            tela.views.append(pagina4)
        elif tela.route=='paginaConfig':
            tela.views.append(pagina5)
        tela.update()
        

    barra_menu = ft.AppBar(
        leading=ft.IconButton(ft.icons.LUNCH_DINING, on_click=lambda e: tela.go(drawer_menu)),
        leading_width=40,
        title=ft.Text('Hamburgueria Voucher', color=ft.colors.RED_400, weight= 'bold', size=30),
        bgcolor=ft.colors.BLACK,
        actions = [
            ft.ElevatedButton(ft.icons.PERSON, ft.colors.RED),
            ft.PopupMenuButton(
                items=[
                ft.PopupMenuItem(text="Tema", icon=ft.icons.SUNNY),
                ft.PopupMenuItem(text="Privacidade",),
                ft.PopupMenuItem(),
                ft.PopupMenuItem(text="Acessibilidade"),
                ],
                icon_color=ft.colors.RED
            )
        ]
    )

    drawer_menu = ft.NavigationDrawer(
        on_change=drawer_change,
        on_dismiss=drawer_dismiss,
        controls=[
            ft.ElevatedButton(text="Página Inicial", icon=ft.icons.HOME, on_click = lambda e: tela.go("/pagina1")),
            ft.ElevatedButton(text="Página de Usuários", icon=ft.icons.PERSON_2, on_click = lambda e: tela.go("/pagina2")),
            ft.ElevatedButton(text="Página de Configurações", icon=ft.icons.SETTINGS, on_click = lambda e: tela.go("/pagina3")),
            ft.ElevatedButton(text="Página de Relatórios", icon=ft.icons.BOOK, on_click = lambda e: tela.go("/pagina4")),
            ft.ElevatedButton(text="Página de Ajuda", icon=ft.icons.HELP, on_click = lambda e: tela.go("/pagina5"))
        ]
    )

    tf_nome = ft.TextField(label='Nome', width=300, color="white", bgcolor="gray")
    tf_numero = ft.TextField(label="Número do contato", width=300, color="white", bgcolor="gray")

    pagina1=ft.View(
        route=("/pagina1"),
        appbar=barra_menu,
        drawer=drawer_menu,
        controls=[
            ft.Text("Página Principal",size=22, color="YELLOW"),
            ft.Text("Bem vindo!",size= 18, color=ft.colors.RED),
            ft.Text("Sinta-se livre para explorar o meu sistema, espero que goste\nCheque o Ícone drawer no canto superior esquerdo e os botões na direita 😎"),
        ]
    )
    pagina2=ft.View(
        route=("/pagina2"),
        appbar=barra_menu,
        drawer=drawer_menu,
        controls=[
            tf_nome,
            tf_numero,
            ft.ElevatedButton(text="Enviar", color=ft.colors.WHITE, bgcolor='gray', on_click=lambda e: tela.add(ft.Text("Dados salvos")))
        ]
    )
    pagina3=ft.View(
        route=("/pagina3"),
        appbar=barra_menu,
        drawer=drawer_menu,
        controls=[
            
        ]
    )
    pagina4=ft.View(
        route=("/pagina4"),
        appbar=barra_menu,
        drawer=drawer_menu,
        controls=[
            
        ]
    )
    pagina5=ft.View(
        route=("/pagina5"),
        appbar=barra_menu,
        drawer=drawer_menu,
        controls=[
            
        ]
    )

    tela.on_route_change=navegação
    tela.go('/pagina1')

ft.app(target=main)