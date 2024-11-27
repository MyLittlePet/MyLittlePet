import flet as ft

def main(page: ft.Page):
    page.title = "Serviços "
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    stack = ft.Stack(
        width=293,
        height=585,
    )

    first_bg = ft.Container(
        width=293,
        height=585,
        border_radius=20,
        bgcolor="#FFDD78",
    )

    second_bg = ft.Container(
        width=293,
        height=456,
        border_radius=15,
        bgcolor="#7D5D42",
    )
    second_bg.top = 126

    third_bg = ft.Container(
        width=293,
        height=58,
        border_radius=20,
        bgcolor="#D0802B",
    )
    third_bg.top = 534

    botao_flecha = ft.Container(
        width=37,
        height=38,
        content=ft.Icon(
            ft.icons.ARROW_BACK,
            size=30,
            color=ft.colors.BLACK,
        ),
        alignment=ft.alignment.center,
        top=10,
        left=5,
        on_click=lambda e: (
            page.overlay.append(ft.AlertDialog(
                title=ft.Text("Você clicou na flecha!")
            )),
            page.update()
        ),
    )

    botao1 = ft.Container(
        width=257,
        height=74,
        border_radius=15,
        bgcolor="#7D8E4E",
        content=ft.Row(
            controls=[
                ft.Container(
                    width=61,
                    height=61,
                    bgcolor="#D9D9D9",
                    border_radius=30.5,
                    alignment=ft.alignment.center,
                ),
                ft.Text(
                    "Lucas Silva da Costa",
                    size=16,
                    weight=ft.FontWeight.W_500,
                    color="#FFFFFF",
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=20,
        ),
        alignment=ft.alignment.center,
    )

    botao2 = ft.Container(
        width=257,
        height=74,
        border_radius=15,
        bgcolor="#7D8E4E",
        content=ft.Row(
            controls=[
                ft.Container(
                    width=61,
                    height=61,
                    bgcolor="#D9D9D9",
                    border_radius=30.5,
                    alignment=ft.alignment.center,
                ),
                ft.Text(
                    "Ana Clara Macedo",
                    size=16,
                    weight=ft.FontWeight.W_500,
                    color="#FFFFFF",
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=20,
        ),
        alignment=ft.alignment.center,
    )

    botao3 = ft.Container(
        width=257,
        height=74,
        border_radius=15,
        bgcolor="#7D8E4E",
        content=ft.Row(
            controls=[
                ft.Container(
                    width=61,
                    height=61,
                    bgcolor="#D9D9D9",
                    border_radius=30.5,
                    alignment=ft.alignment.center,
                ),
                ft.Text(
                    "Julia Soares Espinoza",
                    size=16,
                    weight=ft.FontWeight.W_500,
                    color="#FFFFFF",
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=20,
        ),
        alignment=ft.alignment.center,
    )

    botao4 = ft.Container(
        width=257,
        height=74,
        border_radius=15,
        bgcolor="#7D8E4E",
        content=ft.Row(
            controls=[
                ft.Container(
                    width=61,
                    height=61,
                    bgcolor="#D9D9D9",
                    border_radius=30.5,
                    alignment=ft.alignment.center,
                ),
                ft.Text(
                    "Luiz Mariano Marcos",
                    size=16,
                    weight=ft.FontWeight.W_500,
                    color="#FFFFFF",
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=20,
        ),
        alignment=ft.alignment.center,
    )

    botao_column = ft.Column(
        controls=[botao1, botao2, botao3, botao4],
        spacing=40,
        alignment=ft.MainAxisAlignment.CENTER,
    )
    botao_column.top = 106
    botao_column.left = 18

    servicos_texto = ft.Container(
        width=231,
        height=31,
        border_radius=9,
        bgcolor=ft.colors.BROWN,
        content=ft.Text(
            "Serviços Agendados",
            size=16,
            weight=ft.FontWeight.W_600,
            color=ft.colors.WHITE,
        ),
        alignment=ft.alignment.center,
    )
    servicos_texto.top = 60
    servicos_texto.left = 31

    botao_tela_inicial = ft.Container(
        width=63,
        height=44,
        content=ft.Column(
            controls=[
                ft.Icon(ft.icons.HOME, size=25, color=ft.colors.BLACK),
                ft.Text("Tela Inicial", size=12, color=ft.colors.BLACK, text_align=ft.TextAlign.CENTER),
            ],
            spacing=1,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        alignment=ft.alignment.center,
        data="Tela Inicial",
    )
    botao_tela_inicial.top = 541
    botao_tela_inicial.left = 58

    botao_perfil = ft.Container(
        width=63,
        height=44,
        content=ft.Column(
            controls=[
                ft.Icon(ft.icons.PERSON_ROUNDED, size=24, color=ft.colors.BLACK),
                ft.Text("Perfil", size=12, color=ft.colors.BLACK, text_align=ft.TextAlign.CENTER),
            ],
            spacing=1,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        alignment=ft.alignment.center,
        data="Perfil",
    )
    botao_perfil.top = 541
    botao_perfil.left = 172

    stack.controls.extend([
        first_bg, second_bg, third_bg, botao_flecha, servicos_texto,
        botao_tela_inicial, botao_perfil, botao_column
    ])

    page.add(stack)

ft.app(target=main)
