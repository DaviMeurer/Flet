import flet as ft

def main(page: ft.Page):
    page.auto_scroll=ft.ScrollMode.AUTO
    page.theme_mode=ft.ThemeMode.DARK
    page.window.width=900
    
    listaContatos=[] #lista de dicionário
    
    def salvar_dados(e):
        
        contato = { #dicionário com as infomações atuais do formulário
            "Nome": tf_nome.value,
            "E-mail": tf_email.value,
            "Telefone": tf_tel.value
        }
        
        listaContatos.append(contato)
        
        listaDtRow=[]
        for contato in listaContatos:
            listaDtRow.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(contato["Nome"])),
                        ft.DataCell(ft.Text(contato["E-mail"])),
                        ft.DataCell(ft.Text(contato["Telefone"])),
                    ]
                )
            )  
                     
        tb_contatos.rows=listaDtRow
        
        tf_nome.value=None
        tf_email.value=None
        tf_tel.value=None
        page.update()
        
    
    
    tf_nome =  ft.TextField(label="Nome", bgcolor="gray" )
    tf_email =  ft.TextField(label="E-mail", bgcolor="gray" )
    tf_tel=  ft.TextField(label="Telefone", bgcolor="gray" )
    
    bt_salvar =  ft.ElevatedButton("Salvar", on_click=salvar_dados)
    
    tb_contatos = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Nome")),
            ft.DataColumn(ft.Text("E-mail")),
            ft.DataColumn(ft.Text("Telefone"))
        ]
    )
    
    
    page.add(tf_nome,tf_email,tf_tel,bt_salvar, tb_contatos)
    
ft.app(main)