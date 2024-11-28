import flet as ft

def main(page: ft.Page):
    page.title = "Cadastro"
    page.window_width = 287
    page.window_height = 585
    page.bgcolor = "#FFDD78" 

    background = ft.Container(
        width=287,
        height=585,
        bgcolor="#FFDD78",
    )

    width_2bg = 253.77
    height_2bg = 505

    secundo_bg = ft.Container(
        width=width_2bg,
        height=height_2bg,
        bgcolor="#C2690A",
        top=10
    )

    def on_button_click(e):
        pass

    botao1 = ft.Container(
        width=200,
        height=79,
        border_radius=25,
        bgcolor="#779030",
        content=ft.Text(
            "Sou Pai/Mãe de Pet",
            size=24,
            weight=ft.FontWeight.W_400,
            color=ft.colors.WHITE,
            text_align=ft.TextAlign.CENTER,
            width=400
        ),
        alignment=ft.alignment.center,
        on_click=on_button_click
    )

    espacamento = (height_2bg - (2 * 79)) // 3

    botao1.top = espacamento
    botao1.left = (width_2bg - 200) // 2

    botao2 = ft.Container(
        width=200,
        height=79,
        border_radius=25,
        bgcolor="#779030",
        content=ft.Text(
            "Estou Aqui Para Pets",
            size=24,
            weight=ft.FontWeight.W_400,
            color=ft.colors.WHITE,
            text_align=ft.TextAlign.CENTER,
            width=400
        ),
        alignment=ft.alignment.center,
        on_click=on_button_click
    )
    
    botao2.top = botao1.top + 79 + espacamento
    botao2.left = (width_2bg - 200) // 2

    stack = ft.Stack()
    stack.controls.extend([background, secundo_bg, botao1, botao2])

    page.add(stack)
    page.update()

ft.app(target=main)
