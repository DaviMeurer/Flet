import flet as ft
def main(tela: ft.Page):
    tela.padding=10
    tela.title="Inscrição ao evento Maximus"
    tela.theme_mode=ft.ThemeMode.DARK

    tx_msg = ft.Text(value="Bem Vindo!",color="white")

    tf_nome = ft.TextField(label="Digite o seu nome",width=350,color="dark gray")



    tela.add(tx_msg,tf_nome)

ft.app(target=main)    