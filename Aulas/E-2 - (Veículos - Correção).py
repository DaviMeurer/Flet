import flet as ft

def main(tela: ft.Page):
    tela.theme_mode=ft.ThemeMode.DARK
    
    def valida_marca(e):
        if tf_marca.value=="" or tf_marca.value.strip()=="" :
            tf_marca.error_text="Digite a Marca"
        else:
            tf_marca.error_text=None
        tela.update()
    
    def valida_ano(e):
        ano =  tf_ano.value
        if ano=="":
            tf_ano.error_text="Digite o ano"
        elif not ano.isdigit():
            tf_ano.error_text="Digite um valor númerico"
        elif not (int(ano)>=1886 and int(ano)<=2024):
            tf_ano.error_text="Digite um valor entre 1886 e 2024"
        else:
            tf_ano.error_text=None
        tela.update()
    
    def valida_km(e):
        if not tf_km.value.isdigit():
            tf_km.error_text="Digite um valor"
        elif not (int(tf_km.value)>=0):
            tf_km.error_text="Digite um valor maior que zero"
        else:
            tf_km.error_text=None
        tela.update()
    
    def valida_combustivel(e):
        if op_combustivel.value==None:
            op_combustivel.error_text="Selecione um valor"
        else:
            op_combustivel.error_text=None
        tela.update()
    
    def imprime(e):
        
        if not (tf_marca.error_text or tf_ano.error_text or tf_km.error_text or op_combustivel.error_text):
            tx_dados.value=(
                f"Marca: {tf_marca.value} \n"
                f"Ano: {tf_ano.value} \n"
                f"KM: {tf_km.value} \n"
                f"Tipo de Combustível: {op_combustivel.value} \n"
            )
            
        else:
           tx_dados.value="Preencha os campos"
           tx_dados.color="red"
        tela.update()
    
    
    tf_marca =  ft.TextField(label="Marca", bgcolor="gray", 
                             on_blur=valida_marca)
    tf_ano =  ft.TextField(label="Ano", bgcolor="gray", on_blur=valida_ano)
    tf_km =  ft.TextField(label="Quilometragem", bgcolor="gray",
                          on_blur=valida_km)
    op_combustivel = ft.Dropdown(label="Tipo de Combustível:", 
                                 value="Gasolina",
                                 options=[
                                     ft.dropdown.Option("Gasolina"),
                                     ft.dropdown.Option("Etanol"),
                                     ft.dropdown.Option("Diesel"),
                                     ft.dropdown.Option("Elétrico")
                                 ], on_blur=valida_combustivel)
    
    bt_salvar = ft.ElevatedButton("Salvar", on_click=imprime)
    tx_dados = ft.Text(color="#009977")
    
    
    tela.add(tx_dados,tf_marca,tf_ano,tf_km,op_combustivel,bt_salvar)
    
ft.app(main)