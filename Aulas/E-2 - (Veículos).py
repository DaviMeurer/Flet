import flet
def main(tela=flet.Page):
    tela.title="Cadástro de Veículos"
    tela.scroll=flet.ScrollMode.AUTO
    tela.theme_mode = flet.ThemeMode.DARK
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
        if tf_ano.value.isdigit()==True and tf_ano.value >= 1950 and tf_ano.value <= 2024:
            tf_ano.error_text = None
        else:
            tf_ano.error_text = "Digite um ano válido entre 1950 à 2024"


    tx_marca_titulo = flet.Text("Insira os dados do seu veículo abaixo",color="gray",size=15)
    tf_marca = flet.TextField(label="Marca do veículo", color="gray", width=500,hint_text="Digite a marca do veículo" ,on_blur=valida_marca)
    tf_ano = flet.TextField(label="Ano de Fabricação", width=500, color="gray",hint_text="Digite o ano de fabricação", on_blur=valida_ano)
    tf_quilometragem = flet.TextField(label="Quilometragem rodada", width=500, color="gray",hint_text="Digite a quilometragem rodada",)
    combustivel_opcoes = [
        flet.dropdown.Option("Gasolina"),
        flet.dropdown.Option("Álcool"),
        flet.dropdown.Option("Diesel"),
        flet.dropdown.Option("Elétrico")
    ]
    dd_combustivel = flet.Dropdown(label="Combustivel usado",width=500,options=combustivel_opcoes)


    tela.add(tx_marca_titulo,
            tf_marca,
            tf_ano,
            tf_quilometragem,
            dd_combustivel
    )
flet.app(target=main)