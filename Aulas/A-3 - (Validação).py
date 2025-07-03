import flet as ft
def main(tela: ft.Page):
    tela.title="Inscrição para o Evento"
    tela.theme_mode=ft.ThemeMode.DARK
    tela.scroll=ft.ScrollMode.AUTO
    tela.window_width=600
    tela.spacing=15

    def valida_nome(e):
        lista = tf_nome.value.split()
        if len(lista)<2:
            tf_nome.error_text="Por favor, insira nome e sobrenome"
        else:
            tf_nome.error_text=None
        tela.update()

    def valida_email(e):
        if (tf_email.value.count("@")==1 and tf_email.value.count(".")>=1):
            tf_email.error_text=None
        else:
            tf_email.error_text="E-mail inválido!"
        tela.update()

    def valida_tel(e): #se for só numero tf_tel.value.isdigit()==true
        if not(tf_tel.value.count("(") and tf_tel.value(")") and tf_tel.value("-")):
            tf_tel.error_text="Telefone inválido!"
        else:
            tf_tel.error_text=None
        tela.update()

    tf_nome = ft.TextField(label="Nome: ", width=350, bgcolor="gray",on_blur=valida_nome)
    tf_email = ft.TextField(label="E-Mail: ", width=350, bgcolor="gray",on_blur=valida_email)
    tf_tel = ft.TextField(label="Telefone: ", width=350, bgcolor="gray",on_blur=valida_tel,hint_text="(XX)XXXXX-XXXX")
    
    tela.add(tf_nome,
             tf_email,
             tf_tel,)
    
ft.app(target=main)