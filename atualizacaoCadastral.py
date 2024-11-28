import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.title = "MyLittlePet"
    page.bgcolor = "#FFDD78"
    page.window_width = 287
    page.window_height = 585
    page.padding = 0

    # Componente principal
    main_perfil = ft.Container(
        width=287,
        height=465,
        margin=0,
        padding=0,
        content=ft.Stack(
            [
                # Bloco marrom
                ft.Container(
                    width=250,
                    height=320,
                    bgcolor="#7D5D42",
                    margin=ft.margin.only(top=140, left=10),
                    border_radius=15,
                    padding=0,
                ),
                # Campo de dados
                ft.Container(
                    width=250,
                    height=320,
                    margin=ft.margin.only(top=140, left=5),
                    padding=ft.padding.only(top=15, left=5, right=10),
                    content=ft.Column(
                        [
                            # Campo "Nome"
                            ft.Container(
                                content=ft.Row(
                                    [
                                        ft.Icon(ft.icons.PERSON, color=ft.colors.BLACK),
                                        ft.TextField(label="Nome", bgcolor="#FFDD78"),
                                    ],
                                    spacing=10,
                                    alignment=ft.MainAxisAlignment.START,
                                ),
                                height=50,
                                padding=ft.padding.all(10),
                                border_radius=8,
                            ),
                            # Campo "Registro Geral (RG)"
                            ft.Container(
                                content=ft.Row(
                                    [
                                        ft.Icon(ft.icons.BOOK, color=ft.colors.BLACK),
                                        ft.TextField(label="Registro Geral (RG)", bgcolor="#FFDD78"),
                                    ],
                                    spacing=10,
                                    alignment=ft.MainAxisAlignment.START,
                                ),
                                height=50,
                                padding=ft.padding.all(10),
                                border_radius=8,
                            ),
                            # Campos "Banco" e "Agência"
                            ft.Row(
                                [
                                    ft.Container(
                                        content=ft.Row(
                                            [
                                                ft.Icon(ft.icons.ACCOUNT_BALANCE, color=ft.colors.BLACK),
                                                ft.TextField(label="Banco", bgcolor="#FFDD78"),
                                            ],
                                            spacing=5,
                                            alignment=ft.MainAxisAlignment.START,
                                        ),
                                        height=50,
                                        padding=ft.padding.all(10),
                                        border_radius=8,
                                        expand=True,
                                    ),
                                    ft.Container(
                                        content=ft.Row(
                                            [
                                                ft.Icon(ft.icons.HOME_WORK, color=ft.colors.BLACK),
                                                ft.TextField(label="Agência", bgcolor="#FFDD78", width=90),
                                            ],
                                            spacing=5,
                                            alignment=ft.MainAxisAlignment.START,
                                        ),
                                        height=50,
                                        padding=ft.padding.all(8),
                                        border_radius=8,
                                        expand=True,
                                    ),
                                ],
                                spacing=5,
                            ),
                            # Campo "Conta"
                            ft.Container(
                                content=ft.Row(
                                    [
                                        ft.Icon(ft.icons.CREDIT_CARD, color=ft.colors.BLACK),
                                        ft.TextField(label="Conta", bgcolor="#FFDD78"),
                                    ],
                                    spacing=10,
                                    alignment=ft.MainAxisAlignment.START,
                                ),
                                height=50,
                                padding=ft.padding.all(10),
                                border_radius=8,
                            ),
                            # Botão circular
                            ft.Container(
                                content=ft.ElevatedButton(
                                    content=ft.Icon(ft.icons.REFRESH, color=ft.colors.BLACK),
                                    bgcolor="#7D8E4E",
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=25),
                                        padding=ft.padding.all(0),
                                    ),
                                    width=50,
                                    height=50,
                                ),
                                alignment=ft.alignment.center,
                                margin=ft.margin.only(top=8),
                            ),
                        ],
                        spacing=5,
                        alignment=ft.MainAxisAlignment.START,
                    ),
                ),
                # Ícone no centro (transparente)
                ft.Container(
                    width=110,
                    height=110,
                    bgcolor="#000000",
                    border_radius=50,
                    opacity=0.2,
                    margin=ft.margin.only(top=18, left=82),
                ),
                # Ícone no centro (normal)
                ft.Container(
                    width=110,
                    height=110,
                    bgcolor="#D9D9D9",
                    border_radius=50,
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(top=15, left=80),
                ),
            ]
        ),
    )

    page.add(
        ft.Container(
            content=ft.Column(
                [
                    main_perfil,  # Componente principal
                    ft.NavigationBar(
                        destinations=[
                            ft.NavigationBarDestination(
                                icon=ft.icons.HOME_ROUNDED, label="Tela Inicial"
                            ),
                            ft.NavigationBarDestination(
                                icon=ft.icons.PERSON_ROUNDED, label="Perfil"
                            ),
                        ],
                        bgcolor="#BF5F0B",
                        indicator_color="#DE8A18",
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,  # Alinhamento da coluna principal
            ),
            margin=0,  # Remover margem
            padding=0,  # Remover padding
        )
    )

    # Atualiza a página
    page.update()

# Inicia o app
ft.app(target=main)
