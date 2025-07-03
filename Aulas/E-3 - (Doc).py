import flet as ft
from time import sleep

def main(pg=ft.Page):
    pg.title="Exemplos Gráficos Possíveis"
    pg.window_width=600
    pg.window_height=1000
    pg.padding=13
    pg.spacing=30
    pg.theme_mode=ft.ThemeMode.DARK
    pg.scroll=ft.ScrollMode.AUTO
    pg.update()

    titulo=ft.Text("Exemplos de Comandos Gráficos para Flet",color="yellow",size=20)

    pb = ft.ProgressBar(width=400)
    pg.add(
        titulo,
        ft.Text("Indicador de Barra Linear", style="headlineSmall"),
        ft.Column([ ft.Text("Carregando exemplos..."), pb]),
        ft.Text("Barra Carregando Indeterminadamente", style="headlineSmall"),
        ft.ProgressBar(width=400, color="amber", bgcolor="#eeeeee"),
    )
    for i in range(0, 101):
        pb.value = i * 0.01
        sleep(0.1)
        pg.update()

    a1 = ft.CircleAvatar(
        foreground_image_src="https://avatars.githubusercontent.com/u/5041459?s=88&v=4",
        content=ft.Text("FF"),
    )

    loading = ft.CupertinoActivityIndicator(
            radius=50,
            color=ft.colors.RED,
            animating=True,
           )
    
    lista_icone = ft.Row(
        [
            ft.Icon(name=ft.icons.FAVORITE,color=ft.colors.PINK),
            ft.Icon(name=ft.icons.AUDIOTRACK,color=ft.colors.GREEN_400,size=30),
            ft.Icon(name=ft.icons.BEACH_ACCESS,color=ft.colors.BLUE,size=50),
            ft.Icon(name="settings",color="c1c1c1")
        ]
    )

    img = ft.Image(
        src=f"/icons/icon-512.png",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )

    images = ft.Row(expand=1, wrap=False, scroll="always")
    for i in range(0, 30):
        images.controls.append(
            ft.Image(
                src=f"https://picsum.photos/200/200?{i}",
                width=200,
                height=200,
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
            )
        )
    pg.update()

    pg.add(
        a1,
        loading,
        lista_icone,
        img,
        images,
    )

ft.app(target=main)