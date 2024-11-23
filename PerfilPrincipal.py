import flet as ft

def main(page: ft.Page):
    # Configuração da página
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.title = "MyLittlePet"
    page.bgcolor = "#FFDD78"
    page.window_width = 287
    page.window_height = 585
    page.padding = 0

    # Perfil principal
    main_perfil = ft.Container(
        width=287,
        height=465,
        margin=0,
        padding=0,
        content=ft.Stack(
            [
                # Fundo principal
                ft.Container(
                    width=287,
                    height=450,
                    bgcolor="#7D5D42",
                    margin=ft.margin.only(top=50),
                    border_radius=15,
                    padding=0,
                ),

                # Conteúdo do perfil
                ft.Container(
                    width=240,
                    height=465,
                    border_radius=10,
                    margin=0,
                    padding=0,
                    content=ft.Column(
                        [
                            # Informações do usuário com espaçamento superior
                            ft.Container(
                                content=ft.Row(
                                    [
                                        ft.Container(
                                            width=45,
                                            height=45,
                                            bgcolor="#D9D9D9",  # Fundo cinza para o avatar
                                            border_radius=22,  # Torna o contêiner circular
                                            alignment=ft.alignment.center,
                                            margin=10,
                                        ),
                                        ft.Text(
                                            "Lucas silva",
                                            color=ft.colors.WHITE,
                                            size=22,
                                            weight=ft.FontWeight.BOLD,
                                            expand=True,
                                            text_align=ft.TextAlign.LEFT,
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.START,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    spacing=15,
                                ),
                                margin=ft.margin.only(top=30),  # Espaço acima do Row
                            ),

                            # Container verde para os botões
                            ft.Container(
                                bgcolor="#7D8E4E",  # Fundo verde para os botões
                                width=240,
                                height=200,
                                padding=10,
                                border_radius=10,
                                margin=0,
                                content=ft.Column(
                                    [
                                        # Botão "Conversas"
                                        ft.ElevatedButton(
                                            content=ft.Row(
                                                [
                                                    ft.Icon(
                                                        name=ft.icons.CHAT_BUBBLE,
                                                        color=ft.colors.WHITE,
                                                        size=24,
                                                    ),
                                                    ft.Text(
                                                        "Conversas",
                                                        color=ft.colors.WHITE,
                                                        text_align=ft.TextAlign.LEFT,
                                                    ),
                                                ],
                                                spacing=40,
                                                alignment=ft.MainAxisAlignment.START,
                                                expand=True,
                                            ),
                                            bgcolor="#7D8E4E",
                                            width=240,
                                            height=50,
                                        ),

                                        # Botão "Pagamentos"
                                        ft.ElevatedButton(
                                            content=ft.Row(
                                                [
                                                    ft.Icon(
                                                        name=ft.icons.CHAT_BUBBLE,
                                                        color=ft.colors.WHITE,
                                                        size=24,
                                                    ),
                                                    ft.Text(
                                                        "Pagamentos",
                                                        color=ft.colors.WHITE,
                                                        text_align=ft.TextAlign.LEFT,
                                                    ),
                                                ],
                                                spacing=40,
                                                alignment=ft.MainAxisAlignment.START,
                                                expand=True,
                                            ),
                                            bgcolor="#7D8E4E",
                                            width=240,
                                            height=50,
                                        ),

                                        # Botão "Endereço"
                                        ft.ElevatedButton(
                                            content=ft.Row(
                                                [
                                                    ft.Icon(
                                                        name=ft.icons.CHAT_BUBBLE,
                                                        color=ft.colors.WHITE,
                                                        size=24,
                                                    ),
                                                    ft.Text(
                                                        "Endereço",
                                                        color=ft.colors.WHITE,
                                                        text_align=ft.TextAlign.LEFT,
                                                    ),
                                                ],
                                                spacing=40,
                                                alignment=ft.MainAxisAlignment.START,
                                                expand=True,
                                            ),
                                            bgcolor="#7D8E4E",
                                            width=240,
                                            height=50,
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    spacing=15,
                                ),
                            ),

                            # Novo botão "Serviços Agendados"
                            ft.Container(
                                content=ft.ElevatedButton(
                                    content=ft.Row(
                                        [
                                            ft.Icon(
                                                name=ft.icons.CHECK_BOX,
                                                color=ft.colors.WHITE,
                                                size=24,
                                            ),
                                            ft.Text(
                                                "Serviços Agendados",
                                                color=ft.colors.WHITE,
                                                text_align=ft.TextAlign.LEFT,
                                            ),
                                        ],
                                        spacing=15,
                                        alignment=ft.MainAxisAlignment.START,
                                        expand=True,
                                    ),
                                    bgcolor="#7D8E4E",  # Verde semelhante ao fundo
                                    width=240,
                                    height=65,
                                ),
                                border_radius=0,  # Bordas quadradas
                                width=240,
                                height=65,
                                margin=ft.margin.only(top=25),  # Espaço acima do botão
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=15,  # Espaçamento entre os elementos
                    ),
                ),
            ],
            alignment=ft.alignment.center,
        ),
    )

    # Adiciona a barra de navegação e o perfil dentro de um Container sem margens
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
