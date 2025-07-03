import flet as ft 

def main(pg: ft.Page):
    
    
    def acao_drawer(e):
        match (drawer.selected_index+1):
            case 1:
                pg.go("/")
            case 2:
                pg.go("/novo")
            case 3:
                pg.go("/agenda")
    
    appbar =  ft.AppBar(
        leading=ft.IconButton(ft.icons.MENU, on_click=lambda e: pg.open(drawer)),
        leading_width=40,
        title=ft.Text("Agenda", color="orange"),
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem("Configurações")
                ]
            )
        ]
    )
    
    drawer =  ft.NavigationDrawer(
        on_change=acao_drawer,
        controls=[
            ft.NavigationDrawerDestination(icon=ft.icons.HOME, label="Home"),
            ft.NavigationDrawerDestination(icon=ft.icons.PERSON, label="Novo Contato"),
            ft.NavigationDrawerDestination(icon=ft.icons.CALL_END_OUTLINED, label="agenda")
        ]
        
    )
    
    tf_nome =  ft.TextField(label="Nome")
    tf_numero =  ft.TextField(label="Telefone")
    
    ls_agenda = ft.ListView(
        controls=[
            ft.ListTile(title=ft.Text("Joao Dev", color="orange"),
                        subtitle=ft.Text("67999999", color="orange"), 
                        leading=ft.Icon(ft.icons.PERSON_2_ROUNDED) ),
            ft.ListTile(title=ft.Text("Joao Dev", color="orange"),
                        subtitle=ft.Text("67999999", color="orange"), 
                        leading=ft.Icon(ft.icons.PERSON_2_ROUNDED) ),
            ft.ListTile(title=ft.Text("Joao Dev", color="orange"),
                        subtitle=ft.Text("67999999", color="orange"), 
                        leading=ft.Icon(ft.icons.PERSON_2_ROUNDED) ),
        ]

    )
    
    
    def navecacao(route):
        pg.views.clear()
        
        if pg.route == "/":
            pg.views.append(
                ft.View(
                    route="/",
                    controls=[
                        ft.AppBar(title=ft.Text("Home", color="orange")),
                        ft.Text("Bem vindo a página Home!")
                    ],
                    appbar=appbar,
                    drawer=drawer
                )
            )
        elif pg.route == "/novo":
            pg.views.append(
                ft.View(
                    route="/novo",
                    controls=[
                        ft.AppBar(title=ft.Text("Novo Contato", color="orange")),
                        ft.Text("Cadastre um novo contato!"),
                        tf_nome,
                        tf_numero
                    ],
                    appbar=appbar,
                    drawer=drawer
                )
            )
        elif pg.route == "/agenda":
            pg.views.append(
                ft.View(
                    route="/agenda",
                    controls=[
                        ft.AppBar(title=ft.Text("Agenda", color="orange")),
                        ft.Text("Agenda de contatos"),
                        ls_agenda
                    ],
                    appbar=appbar,
                    drawer=drawer
                )
            )
            
        pg.update()
    
    
    pg.on_route_change=navecacao
    pg.go("/")
    
ft.app(target=main)