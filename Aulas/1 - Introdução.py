#pip install flet
import flet as ft

def main(tela: ft.Page):
    tela.title ="Meu Aplicativo"
    tela.theme_mode = ft.ThemeMode.DARK #cor da tela de fundo

    def acaoBotao(e): #sera chamado quando o botão for clicado
        print("Cliquei") #imprime no terminal quando o botão for clicado
        texto.value="Você Digitou:"+input.value
        tela.update() #atualiza a pagina

    def checkar(e):
        print("ok")
        if cx_selecao.value==True:
            print("Aceitou")
        else:
            print("Não Aceitou")

    #cria os elementos da tela

    #Texto
    titulo =ft.Text("Titulo do meu App", weight="bold", color="blue", italic=True)

    #campo de edição
    input = ft.TextField(label="Digite algo", width="300", bgcolor="gray")

    texto = ft.Text("texto", color="#FFFF00")

    #cria botao que chama a função com nome "acaoBotao"
    botao = ft.ElevatedButton("Salvar", on_click=acaoBotao)

    cx_selecao = ft.Checkbox(label="nunca mais vou faltar!", on_change=checkar)


    #adiciona os elementos na tela
    tela.add(
        titulo,
        input,
        botao,
        texto,
        cx_selecao
    )



#cria o app para computador
ft.app(target=main)