#pip install flet
import flet

def main(tela: flet.Page):
    tela.padding=10
    tela.title="Meu primeiro app"
    tela.theme_mode=flet.ThemeMode.DARK

    def imprime(e):
        print("Volume: ",int(sl_volume.value))
        print("Opção: ",op_opcao.value)
        print("Radio: ",rg_pref.value)

    #texto
    tx_msg = flet.Text("Ctrl + Barra  |  Use e abuse!", color = "#00FF00")  

    #slider
    sl_volume = flet.Slider(min=0, max=16, label="Selecione o Valor", width=300)

    bt_mostra = flet.ElevatedButton(text="Mostra", on_click=imprime)

    #lista de seleção
    opcoes = [
        flet.dropdown.Option("Opção 1"),
        flet.dropdown.Option("Opção 2"),
        flet.dropdown.Option("Opção 3")
    ]
    op_opcao = flet.Dropdown(label="Selecione uma opcão", width=300, options=opcoes)

    #seleção única
    rg_pref = flet.RadioGroup(content=flet.Column([
                            flet.Radio(label="Red",value=1),
                            flet.Radio(label="Green",value=2),
                            flet.Radio(label="Blue",value=3)                                            
    ]))
    tx_imprime = flet.Text(color="FF0000")

    tela.add(tx_msg,
             sl_volume,
             op_opcao,
             rg_pref,
             bt_mostra,
             tx_imprime)

flet.app(target=main)
