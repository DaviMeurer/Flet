import flet
def main(tela: flet.Page):
    tela.padding=15
    tela.window_height=1000
    tela.title=("Inscrição para o evento de turismo Maximus")
    tela.theme_mode=flet.ThemeMode.DARK

    def imprima(e):
        print("\nOs seus Cadastros são estes: \n")
        print("| Nome: ",tf_nome.value,
              "\n| E-mail: ",tf_email.value,
              "\n| Telefone: ",tf_tel.value,
              "\n| Gênero: ",dd_generos.value,
              "\n| País de Residência: ",dd_paises.value,
              "\n| Preferência de Transporte: ",dd_transportes.value,
              "\n| Atividades de Interesse: ")
        if cb_trilhas==True:
            print("- Trilhas\n")
        else: 
            print("- \n")
    
        if cb_canoagem.value==True:
            print("- Canoagem\n")
        else:
            print("- \n")

        if cb_obs_aves.value==True:
            print("- Observação de Aves\n")
        else:
            print("- \n")

        if cb_foto_natureza==True:
            print("- Fotografia da Natureza\n")
        else:
            print("- \n")
        
        if cb_camping.value==True:
            print("- Camping\n")
        else:
            print("- \n")

        print("| Vezes de viagens ao ano: ",sl_frequencia.value)
        print("| Observações adicionais: ",tf_obs.value)                           
        
    tx_titulo = flet.Text("Bem Vindo!\nInsira seus cadastros nos espaços abaixo ",color="white")
    tf_nome = flet.TextField(label="Nome Completo",width=350,color="dark gray")
    tf_email = flet.TextField(label="E-mail",width=350,color="dark gray")
    tf_tel = flet.TextField(label="Número de Telefone", width=350, color="dark gray")
    opcoes_generos = [
        flet.dropdown.Option("Masculino"),
        flet.dropdown.Option("Feminino"),
        flet.dropdown.Option("Prefiro não dizer")
    ]
    opcoes_paises = [
        flet.dropdown.Option("Argentina"),
        flet.dropdown.Option("Bolívia"),
        flet.dropdown.Option("Brasil"),
        flet.dropdown.Option("Chile"),
        flet.dropdown.Option("Colômbia"),
        flet.dropdown.Option("Equador"),
        flet.dropdown.Option("Guiana"),
        flet.dropdown.Option("Paraguai"),
        flet.dropdown.Option("Peru"),
        flet.dropdown.Option("Suriname"),
        flet.dropdown.Option("Venezuela")
    ]
    opcoes_transportes = [
        flet.dropdown.Option("Carro"),
        flet.dropdown.Option("Avião"),
        flet.dropdown.Option("Ônibus"),
        flet.dropdown.Option("Bicicleta"),
        flet.dropdown.Option("A pé")
    ]
    dd_generos = flet.Dropdown(label="Gênero", width="350", color="dark gray", options=opcoes_generos)
    dd_paises = flet.Dropdown(label="País de Residência", width= 350, color= "dark gray", options=opcoes_paises)
    dd_transportes = flet.Dropdown(label="Meio de transporte",width=350,color="dark gray",options=opcoes_transportes)
    tx_msg = flet.Text("\nAtividades de Interesse",size= 16)
    cb_trilhas = flet.Checkbox(label="Trilhas",width=200)
    cb_canoagem = flet.Checkbox(label="Canoagem",width=200)
    cb_obs_aves = flet.Checkbox(label="Observação de aves",width=200)
    cb_foto_natureza = flet.Checkbox(label="Fotografia da Natureza",width=200)
    cb_camping = flet.Checkbox(label="Camping",width=200)
    sl_frequencia = flet.Slider(label="Frequência de viagens (vezes ao ano)",min=1,max=15,width=400)
    tf_obs = flet.TextField(label="Observações adicionais",width=350,color="dark gray")
    eb_salvar = flet.ElevatedButton(text="Salvar",width=90,color="dark gray",on_click=imprima)
    

    tela.add(tx_titulo,
             tf_nome,
             tf_email,
             tf_tel,
             dd_generos,
             dd_paises,
             dd_transportes,
             tx_msg,
             cb_trilhas,
             cb_canoagem,
             cb_obs_aves,
             cb_foto_natureza,
             cb_camping,
             sl_frequencia,
             tf_obs,
             eb_salvar,)

flet.app(target=main)    