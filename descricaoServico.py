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
                    height=460,
                    bgcolor="#7D5D42",
                    margin=ft.margin.only(top=50),
                    border_radius=15,
                ),
                
                
                ft.Container(
                    width=240,
                    height=270,
                    bgcolor="#7D8E4E",
                    border_radius=15,
                    margin=ft.margin.only(top=50),
                    padding=0,
                    content=ft.Column(  
                        [
                            ft.Row(
                                [
                                    ft.Icon(name=ft.icons.PEOPLE, color="black", size=24),  
                                    ft.Text("Lucas da Silva Costa", color="white", size=18, weight="bold"),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,  
                                spacing=10, 
                            ),
                            ft.Row(
                                [
                                    ft.Icon(name=ft.icons.CALENDAR_MONTH_OUTLINED, color="black", size=24),  
                                    ft.Text("10/04/2024", color="white", size=18, weight="bold"),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,  
                                spacing=10,  
                            ),
                            ft.Row(
                                [
                                    ft.Icon(name=ft.icons.PETS, color="black", size=24),  
                                    ft.Text("gato", color="white", size=18, weight="bold"),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,  
                                spacing=10,  
                            ),
                            ft.Row(
                                [
                                    ft.Icon(name=ft.icons.LOCK_CLOCK, color="black", size=24),  
                                    ft.Text("14h", color="white", size=18, weight="bold"),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,  
                                spacing=10,  
                            ),
                            ft.Container(
                                alignment=ft.alignment.center,
                                margin=ft.margin.only(top=20),
                                content=ft.ElevatedButton(
                                    content=ft.Container(
                                        content=ft.Icon(name=ft.icons.MESSAGE, color=ft.colors.WHITE),
                                        width=40,
                                        height=40,
                                    ),
                                    bgcolor='#8C5120',
                                ),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,  
                        spacing=15,  
                    ),
                ),

                
                ft.Container(
                    content=ft.Text("Informações", color="white", size=18, weight="bold"),
                    bgcolor="#8B4513",
                    width=200,
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
