import flet as ft

def main(tela: ft.Page):
    tela.title="Cadastração de Pontos Turísticos"
    tela.auto_scroll=ft.ScrollMode.AUTO
    tela.theme_mode=ft.ThemeMode.DARK
    tela.padding=15
    tela.spacing=20

    lista_dicionarios = [] #guardar os dicionarios

    def salvar_dados(e):
        pontos_t = {
            "Ponto Turístico":tf_pontoTuristico.value,
            "Localização":tf_loc.value,
            "Categoria":dd_categorias.value,
            "Avalização":sl_nota.value,
            "Disponível ao Público?":cb_publico.value
        }

    listaRow=I

    tx_titulo = ft.Text("Bem Vindo!\nPor favor, cadastre o(s) seu(s) ponto(s) turístico(s)",size=16,color="Yellow",)
    tf_pontoTuristico = ft.TextField(label="Ponto Turístico",color='gray',width=300)
    tf_loc = ft.TextField(label="Localização (Rua, n° da casa, etc)",color="gray",width=300)
    
    opcoes_categorias = [
        ft.dropdown.Option("Histórico"),
        ft.dropdown.Option("Natural"),
        ft.dropdown.Option("Cultural"),
        ft.dropdown.Option("Entretenimento"),
        ft.dropdown.Option("Religioso"),
        ft.dropdown.Option("Arquitetônico"),
        ft.dropdown.Option("Urbano"),
        ft.dropdown.Option("Aventura"),
        ft.dropdown.Option("Gastronômico")
    ]

    dd_categorias = ft.Dropdown(label="Categoria do ponto turístico",width=300,color="gray",options=opcoes_categorias)
    tx_nota = ft.Text("Avaliação do ponto turístico",size=15,color='bright blue')
    sl_nota = ft.Slider(label="{value}⭐",divisions=5,min=0,max=5,width=350,value=0)
    cb_publico = ft.Checkbox(label="Está aberto ao público?", width=300)
    bt_salvar = ft.ElevatedButton(text='Salvar', width=250, color= "bright red", on_click=salvar_dados)

    tela.add(tx_titulo,
             tf_pontoTuristico,
             tf_loc,
             dd_categorias,
             tx_nota,
             sl_nota,
             cb_publico,
             )

ft.app(target=main)
