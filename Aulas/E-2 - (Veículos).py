import flet as ft
def main(tela=ft.Page):
    tela.title="Cadástro de Veículos"
    tela.scroll=ft.ScrollMode.AUTO
    tela.theme_mode = ft.ThemeMode.DARK
    tela.window_width = "850"
    tela.window_height = "800"
    tela.padding=13
    tela.spacing=10

    def valida_marca(e):
        lista = tf_marca.value.split()
        if len(lista)<1:
            tf_marca.error_text="Por favor, insira nome e sobrenome"
        else:
            tf_marca.error_text=None
        tela.update()

    def valida_ano(e):
        if tf_ano.value.isdigit()==True and tf_ano.value.isdigit() <= 2024 and tf_ano.value.isdigit() >= 1950:
            tf_ano.error_text = None
        else:
            tf_ano.error_text = "Digite um ano válido entre 1950 à 2024"
        tela.update

    def valida_quilometragem(e):
        if tf_quilometragem.value.isdigit==True and tf_quilometragem.value()>=0:
            tf_quilometragem.error_text="Digite um número válido de no mínimo 0 km"
        else:
            tf_quilometragem.error_text=None
        tela.update

    def salvar(e):
        tx_marca_titulo.value
        tela.update


    tx_marca_titulo = ft.Text("Insira os dados do seu veículo abaixo",color="gray",size=15)
    tf_marca = ft.TextField(label="Marca do veículo", color="gray", width=500,hint_text="Digite a marca do veículo" ,on_blur=valida_marca)
    tf_ano = ft.TextField(label="Ano de Fabricação", width=500, color="gray",hint_text="Digite o ano de fabricação", on_blur=valida_ano)
    tf_quilometragem = ft.TextField(label="Quilometragem rodada", width=500, color="gray",hint_text="Digite a quilometragem rodada",on_blur=valida_quilometragem)
    combustivel_opcoes = [
        ft.dropdown.Option("Gasolina"),
        ft.dropdown.Option("Álcool"),
        ft.dropdown.Option("Diesel"),
        ft.dropdown.Option("Elétrico")
    ]
    dd_combustivel = ft.Dropdown(label="Combustivel usado",width=500,color="gray",hint_text="Digite o combustível usado",options=combustivel_opcoes)
    bt_salvar = ft.ElevatedButton(text="Salvar",color="gray",on_click=salvar)
    tx_resultados = ft.Text(label="")

    tela.add(tx_marca_titulo,
            tf_marca,
            tf_ano,
            tf_quilometragem,
            dd_combustivel,
            bt_salvar,
    )
ft.app(target=main)