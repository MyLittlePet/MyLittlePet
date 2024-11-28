import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.title = "MyLittlePet"
    page.bgcolor = "#FFDD78"
    page.window_width = 287
    page.window_height = 585
    page.padding = 0

    main_perfil = ft.Container(
        width=287,
        height=465,
        margin=0,
        padding=0,
        content=ft.Stack(
            [
                ft.Container(
                    width=287,
                    height=450,
                    bgcolor="#7D5D42",
                    margin=ft.margin.only(top=50),
                    border_radius=15,
                    padding=0,
                ),
               
                ft.Container(
                    width=240,
                    height=465,
                    border_radius=10,
                    margin=0,
                    padding=0,
                    content=ft.Column(
                        [
                            ft.Container(
                                content=ft.Row(
                                    [
                                        ft.Container(
                                            width=45,
                                            height=45,
                                            bgcolor="#D9D9D9",  
                                            border_radius=22,  
                                            alignment=ft.alignment.center,
                                            margin=10,
                                        ),
                                        ft.Text(
                                            "Lucas Silva",
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
                                margin=ft.margin.only(top=30),  
                            ),
                            
                            ft.Column(
                                [
                                    ft.Container(
                                        content=ft.ElevatedButton(
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
                                            bgcolor="#DFAF21",
                                            width=240,
                                            height=60,
                                        ),
                                        bgcolor="#DFAF21",
                                        padding=0,
                                        margin=0,
                                        border_radius=10,
                                    ),
                                    ft.Container(
                                        content=ft.ElevatedButton(
                                            content=ft.Row(
                                                [
                                                    ft.Icon(
                                                        name=ft.icons.MONEY,
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
                                            bgcolor="#DFAF21",
                                            width=240,
                                            height=60,
                                        ),
                                        bgcolor="#DFAF21",
                                        padding=0,
                                        margin=ft.margin.only(top=5),  # Menor espaço entre os botões
                                        border_radius=10,
                                    ),
                                    ft.Container(
                                        content=ft.ElevatedButton(
                                            content=ft.Row(
                                                [
                                                    ft.Icon(
                                                        name=ft.icons.LOCATION_ON_SHARP,
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
                                            bgcolor="#DFAF21",
                                            width=240,
                                            height=60,
                                        ),
                                        bgcolor="#DFAF21",
                                        padding=0,
                                        margin=ft.margin.only(top=5),  # Menor espaço entre os botões
                                        border_radius=10,
                                    ),
                                ],
                                spacing=0,  # Remove espaçamento adicional entre os containers
                            ),
                            # Novo botão "Serviços Agendados"
                            ft.Container(
                                content=ft.ElevatedButton(
                                    content=ft.Row(
                                        [
                                            ft.Text(
                                                "Serviços Agendados",
                                                color=ft.colors.WHITE,
                                                text_align=ft.TextAlign.LEFT,
                                            ),
                                            ft.Icon(
                                                name=ft.icons.CHECK_BOX,
                                                color=ft.colors.WHITE,
                                                size=24,
                                            ),
                                        ],
                                        spacing=15,
                                        alignment=ft.MainAxisAlignment.START,
                                        expand=True,
                                    ),
                                    bgcolor="#DFAF21",  
                                    width=240,
                                    height=65,
                                ),
                                border_radius=10,  
                                width=240,
                                height=65,
                                margin=ft.margin.only(top=25),
                                bgcolor="#DFAF21",
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=15,  
                    ),
                ),
            ],
            alignment=ft.alignment.center,
        ),
    )
    
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    main_perfil,  
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
                alignment=ft.MainAxisAlignment.START,  
            ),
            margin=0,  
            padding=0,  
        )
    )

    
    page.update()


ft.app(target=main)
