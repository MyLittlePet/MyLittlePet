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
                    height=350,
                    bgcolor="#7D5D42",
                    margin=ft.margin.only(top=115),
                    border_radius=10,
                ),
                
                
                ft.Container(
                    width=240,
                    height=270,
                    border_radius=15,
                    margin=ft.margin.only(top=70),
                    padding=0,
                    alignment=ft.alignment.center,
                    content=ft.Column(  
                        [
                            ft.Container(
                                alignment=ft.alignment.center,
                                margin=ft.margin.only(top=20),
                                content=ft.ElevatedButton(
                                    content=ft.Container(
                                        content=ft.Row(
                                            [
                                                ft.Icon(name=ft.icons.MONEY, color=ft.colors.WHITE),
                                                ft.Text("Dinheiro", color="white", size=16, weight="bold")
                                            ],
                                            spacing=50,
                                        )
                                    ),
                                    bgcolor='#DFAF21',
                                    width=230,
                                    height=55
                                ),
                                width=230,
                                height=55,
                                bgcolor='#DFAF21',
                                border_radius=8,
                            ),
                            
                            ft.Container(
                                alignment=ft.alignment.center,
                                margin=ft.margin.only(top=20),
                                content=ft.ElevatedButton(
                                    content=ft.Container(
                                        content=ft.Row(
                                            [
                                                ft.Icon(name=ft.icons.CREDIT_CARD, color=ft.colors.WHITE),
                                                ft.Text("Cartão", color="white", size=16, weight="bold")
                                            ],
                                            spacing=50,
                                        ),
                                        width=200,
                                        height=40,
                                    ),
                                    bgcolor='#DFAF21',
                                    width=230,
                                    height=55
                                ),
                                width=230,
                                height=55,
                                bgcolor='#DFAF21',
                                border_radius=8,
                            ),
                            
                            ft.Container(
                                alignment=ft.alignment.center,
                                margin=ft.margin.only(top=20),
                                content=ft.ElevatedButton(
                                    content=ft.Container(
                                        content=ft.Row(
                                            [
                                                ft.Icon(name=ft.icons.DIAMOND, color=ft.colors.WHITE),
                                                ft.Text("PIX", color="white", size=16, weight="bold")
                                            ],
                                            spacing=60,
                                        ),
                                        width=230,
                                        height=40,
                                    ),
                                    bgcolor='#DFAF21',
                                    width=230,
                                    height=55
                                ),
                                width=230,
                                height=55,
                                bgcolor='#DFAF21',
                                border_radius=8,
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,  
                        spacing=15,
                    ),
                ),

                
                ft.Container(
                    content=ft.Text("Formas de pagamento", color="white", size=18, weight="bold"),
                    bgcolor="#8B4513",
                    width=230,
                    height=40,
                    border_radius=20,
                    alignment=ft.alignment.center,
                    margin=ft.margin.only(bottom=350),
                    border=ft.border.all(1, ft.colors.BLACK),
                ),
            ],
            alignment=ft.alignment.center
        )
    )

    page.add(
        ft.Column(
            [
                main_perfil,  
                ft.Container(expand=True),  
                ft.NavigationBar(
                    destinations=[
                        ft.NavigationBarDestination(icon=ft.icons.HOME_ROUNDED, label="Tela Inicial"),
                        ft.NavigationBarDestination(icon=ft.icons.PERSON_ROUNDED, label="Perfil"),
                    ],
                    bgcolor="#BF5F0B",
                    indicator_color="#DE8A18",
                ),
            ],
            spacing=0, 
        )
    )
    
    page.update()

ft.app(target=main)