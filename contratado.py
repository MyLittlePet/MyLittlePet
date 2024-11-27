import flet as ft

def main(page: ft.Page):
    page.title = "Contratado"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    stack = ft.Stack()

    first_bg = ft.Container(
        width=287.38,
        height=585,
        bgcolor="#FFDD78",
        top=-36,
        left=-13,
    )

    second_bg = ft.Container(
        width=246,
        height=500,
        bgcolor="#C2690A",
        top=10,
        left=10,
    )

    contratado = ft.Container(
        width=150,
        height=25,
        bgcolor=ft.colors.GREEN,
        border_radius=20,
        content=ft.Row(
            controls=[ft.Text(
                value="Sou Contratado",
                size=18,
                weight="w400",
                color=ft.colors.WHITE
            )],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        top=30,
        left=65
    )

    nome_completo = ft.Column(
        controls=[ 
            ft.Text("Nome Completo", size=16, weight="w600", color=ft.colors.WHITE),
            ft.TextField(
                label=None,
                bgcolor=ft.colors.WHITE,
                border_color=ft.colors.BLACK,
                border_width=1,
                width=184,
                height=35,
                text_style=ft.TextStyle(color=ft.colors.BLACK),
            ),
        ],
        spacing=5,
        horizontal_alignment=ft.CrossAxisAlignment.START,
    )

    nome_completo.top = 60
    nome_completo.left = 40

    registro_geral = ft.Column(
        controls=[ 
            ft.Text("Registro Geral (RG)", size=16, weight="w600", color=ft.colors.WHITE),
            ft.TextField(
                label=None,
                bgcolor=ft.colors.WHITE,
                border_color=ft.colors.BLACK,
                border_width=1,
                width=184,
                height=35,
                text_style=ft.TextStyle(color=ft.colors.BLACK),
            ),
        ], 
        spacing=5,
        horizontal_alignment=ft.CrossAxisAlignment.START,
    )

    registro_geral.top = 130
    registro_geral.left = 40

    servicos = ft.Column(
        controls=[ 
            ft.Text("Serviços Ofertados", size=16, weight="w600", color=ft.colors.WHITE),
            ft.Dropdown(
                options=[
                    ft.dropdown.Option("Banho e Tosa"),
                    ft.dropdown.Option("Consultas Veterinárias"),
                    ft.dropdown.Option("Vacinação"),
                    ft.dropdown.Option("Hospedagem"),
                    ft.dropdown.Option("Rações e Petiscos"),
                    ft.dropdown.Option("Produtos de Higiene"),
                    ft.dropdown.Option("Acessórios para Pets"),
                ],
                label="Escolha um serviço",
                bgcolor=ft.colors.WHITE,
                border_color=ft.colors.BLACK,
                border_width=1,
                width=184,
                height=45,
                text_style=ft.TextStyle(color=ft.colors.BLACK),
            ),
        ],
        spacing=5,
        horizontal_alignment=ft.CrossAxisAlignment.START,
    )

    servicos.top = 200
    servicos.left = 40

    dados_bancarios = ft.Column(
        controls=[
            ft.Text("Dados Bancários", size=16, weight="w600", color=ft.colors.WHITE),
            ft.TextField(
                label="Número do Banco",
                bgcolor=ft.colors.WHITE,
                border_color=ft.colors.BLACK,
                border_width=1,
                width=184,
                height=35,
                text_style=ft.TextStyle(color=ft.colors.BLACK),
            ),
            ft.TextField(
                label="Agência",
                bgcolor=ft.colors.WHITE,
                border_color=ft.colors.BLACK,
                border_width=1,
                width=184,
                height=35,
                text_style=ft.TextStyle(color=ft.colors.BLACK),
            ),
            ft.TextField(
                label="Conta",
                bgcolor=ft.colors.WHITE,
                border_color=ft.colors.BLACK,
                border_width=1,
                width=184,
                height=35,
                text_style=ft.TextStyle(color=ft.colors.BLACK),
            ),
        ],
        spacing=5,
        horizontal_alignment=ft.CrossAxisAlignment.START,
    )

    dados_bancarios.top = 280
    dados_bancarios.left = 40

    play_button = ft.Container(
        width=136,
        height=37,
        border_radius=25,
        bgcolor=ft.colors.GREEN,
        alignment=ft.alignment.center,
        content=ft.Icon(
            name=ft.icons.PLAY_ARROW,
            color=ft.colors.BLACK,
            size=45,
        ),
    )

    play_button.top = 450
    play_button.left = 60

    stack.controls.append(first_bg)
    stack.controls.append(second_bg)
    stack.controls.append(contratado)
    stack.controls.append(nome_completo)
    stack.controls.append(registro_geral)
    stack.controls.append(servicos)
    stack.controls.append(dados_bancarios)
    stack.controls.append(play_button)

    page.add(stack)

ft.app(target=main)
