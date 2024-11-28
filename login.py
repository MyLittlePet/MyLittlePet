import flet as ft

def main(page: ft.Page):
    page.title = "Tela de Login"
    page.bgcolor = "#FFDD78"

    page.window.width = 287
    page.window.height = 585

    background = ft.Container(
        width=287,
        height=585,
        bgcolor="#FFDD78",
    )

    segundo_bg = ft.Container(
        width=253.77,
        height=505,
        bgcolor="#C2690A",
    )

 
    stack = ft.Stack()

    stack.controls.append(background)
    stack.controls.append(segundo_bg)

   
    stack.controls.append(
        ft.Container(
            top=20, 
            left=50, 
            content=ft.Column(
                controls=[ 
                    ft.Container(
                        width=157,
                        height=46,
                        border_radius=20,
                        bgcolor="#779030",
                        content=ft.Column(
                            controls=[ft.Text("Login", color="white", size=24)],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=10,
            ),
        )
    )

    
    stack.controls.append(
        ft.Container(
            top=80,  
            left=20,  
            content=ft.Column(
                controls=[ 
                    ft.Text("Email", color="white", size=20),
                    ft.TextField(
                        width=205.97,
                        height=35,
                        border_radius=5,
                        bgcolor="white",
                        color="black",
                    ),
                    ft.Text("Senha", color="white", size=20),
                    ft.TextField(
                        width=205.97,
                        height=35,
                        border_radius=5,
                        bgcolor="white",
                        color="black",
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=10,
            ),
        )
    )

   
    stack.controls.append(
        ft.Container(
            top=230,  
            left=10,  
            content=ft.Column(
                controls=[
                    ft.TextButton(
                        "Esqueceu a sua senha?",
                        style=ft.ButtonStyle(color="#000000"),
                    ),
                    ft.Row(
                        controls=[
                            ft.Text("Não tem uma conta ainda?", size=10, weight=ft.FontWeight.W_400, color="#000000"),
                            ft.TextButton(
                                "Registrar agora",
                                style=ft.ButtonStyle(
                                    color=ft.colors.GREY,
                                    bgcolor="#C2690A",
                                    padding=ft.Padding(top=0, right=0, bottom=0, left=1),
                                ),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        spacing=10,
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=10,
            ),
        )
    )

   
    stack.controls.append(
        ft.Container(
            top=350, 
            left=20, 
            content=ft.ElevatedButton(
                content=ft.Text("Google"),
                on_click=lambda e: None,
                bgcolor=ft.colors.WHITE,
                color="red",
                width=207,
                height=40,
                style=ft.ButtonStyle(
                    text_style=ft.TextStyle(size=15, weight=ft.FontWeight.W_700)
                ),
            ),
        )
    )

    stack.controls.append(
        ft.Container(
            top=400,  
            left=20, 
            content=ft.ElevatedButton(
                content=ft.Text("Facebook"),
                on_click=lambda e: None,
                bgcolor=ft.colors.WHITE,
                color="blue",
                width=207,
                height=40,
                style=ft.ButtonStyle(
                    text_style=ft.TextStyle(size=15, weight=ft.FontWeight.W_700)
                ),
            ),
        )
    )

    stack.controls.append(
        ft.Container(
            top=450,  
            left=50,  
            content=ft.ElevatedButton(
                content=ft.Icon(ft.icons.PLAY_ARROW),
                on_click=lambda e: None,
                bgcolor="#779030",
                color="black",
                width=136,
                height=38,
            ),
        )
    )

    page.add(stack)

ft.app(target=main)
