import flet as ft
def main(tela:ft.Page):
    tela.theme_mode = ft.ThemeMode.LIGHT
    tela.auto_scroll = ft.ScrollMode.AUTO
    tela.title = "Le Navegations"

    def drawer_change(e):
        print("Chamei a gaveta")

    def drawer_dismiss(e):
        print(f"Selecionei: {drawer_menu.selected_index}")

    def navegação(route):
        tela.views.clear()
        if tela.route=='/pagina1':
            tela.views.append(pagina1)
        elif tela.route=="/pagina2":
            tela.views.append(pagina2)
        elif tela.route=="/pagina3":
            tela.views.append(pagina3)
        tela.update()

    barra_menu = ft.AppBar(
        leading=ft.IconButton(ft.icons.MENU, on_click=lambda e: tela.open(drawer_menu)),
        leading_width=40,
        title=ft.Text("App Senac", color=ft.colors.BLUE_800, weight='bold'),
        bgcolor=ft.colors.ORANGE_400,
        actions = [
            ft.ElevatedButton(ft.icons.SEARCH, ft.colors.WHITE, on_click = lambda e: 'Cliquei Search'),
            ft.ElevatedButton(ft.icons.SETTINGS, ft.colors.WHITE,on_click = lambda e: 'Cliquei Settings'),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text='Perfil', icon=ft.icons.PERSON),
                    ft.PopupMenuItem(text='Privacidade'),
                    ft.PopupMenuItem(),
                    ft.PopupMenuItem(text='info', checked = False)
                ],
                icon_color=ft.colors.WHITE
        )
      ]
    )

    drawer_menu = ft.NavigationDrawer(

        on_change=drawer_change,
        on_dismiss=drawer_dismiss,
        controls=[
            ft.NavigationDrawerDestination(
                label="Fornecedores",
                icon=ft.icons.SHOPPING_CART
            ),
            ft.NavigationDrawerDestination(
                label="Clientes",
                icon=ft.icons.PERSON_2
            ),
            ft.NavigationDrawerDestination(
                label='Colaboradores',
                icon=ft.icons.PEOPLE
            )
        ]
    )

    pagina1 = ft.View(
        route="/pagina1",
        appbar=barra_menu,
        drawer=drawer_menu,
        controls=[
            ft.Text("Pagina 1", style="headlineMedium"),
            ft.Image(src='src/Spiffo.jpg',width=600),
            ft.ElevatedButton(text="Ir para a página 2", on_click = lambda e: tela.go("/pagina2")),
            ft.ElevatedButton(text="Ir para a página 3", on_click = lambda e: tela.go("/pagina3"))
        ]
    )
    pagina2 = ft.View(
        route="/pagina2",
        appbar=barra_menu,
        drawer=drawer_menu,
        controls=[
            ft.Text("Pagina 2", style="headlineMedium"),
            ft.Image(src='src/Toby_Fox.png',width=300),
            ft.ElevatedButton(text="Ir para a página 3",  on_click = lambda e: tela.go("/pagina3")),
            ft.ElevatedButton(text="Ir para a página 1",  on_click = lambda e: tela.go("/pagina1")),
        ]
    )
    pagina3 = ft.View(
        route="/pagina3",
        appbar=barra_menu,
        drawer=drawer_menu,
        controls=[
            ft.Text("Pagina 3", style="headlineMedium"),
            ft.Image(src='src/Undertale.jpg',width=300),
            ft.Image(src="src/Deltarune.jpg", width=300),
            ft.ElevatedButton(text="Ir para a página 1",  on_click = lambda e: tela.go("/pagina1")),
            ft.ElevatedButton(text="Ir para a página 2",  on_click = lambda e: tela.go("/pagina2"))
        ]
    )


    tela.on_route_change=navegação
    tela.go('/pagina1')

ft.app(target=main)