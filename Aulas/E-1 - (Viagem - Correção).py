import flet as ft 

def main(tela: ft.Page):
    tela.title="Inscrição para o Evento"
    tela.theme_mode=ft.ThemeMode.DARK
    tela.scroll=ft.ScrollMode.AUTO
    tela.window_width=600
    tela.spacing=15

    def imprime(e):
        str_resultado = (f"Nome: {tf_nome.value}"
                         f"\nE-Mail: {tf_email.value}"
                         f"\nTelefone: {tf_tel.value}"
                         f"\nSexo: {dp_genero.value}"
                         f"\nPaís: {dp_pais.value}"
                         f"\nTransporte: {dp_transporte.value}"
                         f"\nAtividades de Interesse: \n"
                         )
        
        for atividade in cx_atividades:
            if atividade.value==True:
                str_resultado += atividade.label+"\n"
        
        str_resultado +=(
            f"Frequência: {sl_freq.value}"
            f"\nObs: {tf_obs.value}"
        )
        
        
        tx_imprime.value=str_resultado
        tela.update()


    tf_nome = ft.TextField(label="Nome:", width=350, bgcolor="gray")
    tf_email = ft.TextField(label="E-Mail:", width=350, bgcolor="gray")
    tf_tel = ft.TextField(label="Telefone:", width=350, bgcolor="gray",
                           hint_text="(XX)XXXXX-XXXX")

    dp_genero =  ft.Dropdown(label="Selecione o Genero:", options=[
        ft.dropdown.Option(key="Masculino"),
        ft.dropdown.Option(key="Feminino")
    ], width=350)

    dp_pais = ft.Dropdown(label="Selecione o País:", options=[
        ft.dropdown.Option(key="Brasil"),
        ft.dropdown.Option(key="Argentina")
    ], width=350)

    dp_transporte = ft.Dropdown(label="Selecione seu meio de transporte:",
       options=[
        ft.dropdown.Option(key="Carro"),
        ft.dropdown.Option(key="Moto Eletrica"),
        ft.dropdown.Option(key="Avião")
        ],
    width=350)

    

    cx_atividades =  ( #tupla é imutavel
        ft.Checkbox(label="Trilha"),
        ft.Checkbox(label="Canoagem"),
        ft.Checkbox(label="Camping")
    )

    tx_freq = ft.Text("Selecione a Frequência de Viagens:")
    sl_freq = ft.Slider(label="Frequência de Viagens: {value}", divisions=15, min=0, 
                        max=15, value=0)


    tf_obs = ft.TextField(label="Observação:", width=350, bgcolor="gray",
                          multiline=True)

    bt_salvar = ft.ElevatedButton(text="Enviar", on_click=imprime)


    tx_imprime =  ft.Text(color="#00FFFF")


    tela.add(tf_nome,tf_email,tf_tel,dp_genero,
             dp_pais,dp_transporte, *cx_atividades,tx_freq, 
             sl_freq,tf_obs,bt_salvar,tx_imprime)
    #*cx_atividades é a mesma coisa que eu fazer isso:
    #for i in cx_atividades:
    #    tela.add(i)

ft.app(target=main)