import flet as ft
import requests
def main(pg:ft.Page):
    pg.theme_mode=ft.ThemeMode.DARK
    pg.scroll=ft.ScrollMode.AUTO
    
    url = "https://pokeapi.co/api/v2/pokemon/"

    pesquisa = requests.get(url)

    dados = pesquisa.json()

    print(dados["results"][250]["name"])

    pg.add(

    )

ft.app(target=main)