#pip install flet
import flet as ft

def main(tela: ft.Page):
    tela.padding=10
    tela.title="Meu primeiro app"
    tela.theme_mode=ft.ThemeMode.DARK

    def imprime(e):
        print("Volume: ",int(sl_volume.value))
        print("Opção: ",op_opcao.value)
        print("Radio: ",rg_pref.value)

    #texto
    tx_msg = ft.Text("Ctrl + Barra  |  Use e abuse!", color = "#00FF00")  

    #slider
    sl_volume = ft.Slider(min=0, max=16, label="Selecione o Valor", width=300)

    bt_mostra = ft.ElevatedButton(text="Mostra", on_click=imprime)

    #lista de seleção
    opcoes = [
        ft.dropdown.Option("Opção 1"),
        ft.dropdown.Option("Opção 2"),
        ft.dropdown.Option("Opção 3")
    ]
    op_opcao = ft.Dropdown(label="Selecione uma opcão", width=300, options=opcoes)

    #seleção única
    rg_pref = ft.RadioGroup(content=ft.Column([
                            ft.Radio(label="Red",value=1),
                            ft.Radio(label="Green",value=2),
                            ft.Radio(label="Blue",value=3)                                            
    ]))
    tx_imprime = ft.Text(color="FF0000")

    tela.add(tx_msg,
             sl_volume,
             op_opcao,
             rg_pref,
             bt_mostra,
             tx_imprime)

ft.app(target=main)
