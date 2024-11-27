import flet as ft

def main(page: ft.Page):
    page.title = "Página de Login"
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

    login = ft.Container(
        width=157,
        height=46,
        bgcolor=ft.colors.GREEN,
        border_radius=20,
        content=ft.Row(
            controls=[ft.Text(
                value="LOGIN", 
                size=18, 
                weight="w400", 
                color=ft.colors.WHITE
            )],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        top=30,
        left=65
    )

    email = ft.Column(
        controls=[ 
            ft.Text("Email", size=16, weight="w600", color=ft.colors.WHITE),
            ft.TextField(
                label=None,
                hint_text="Digite seu email",
                bgcolor=ft.colors.WHITE,
                border_color=ft.colors.BLACK,
                border_width=1,
                width=200,
                height=40,
                text_style=ft.TextStyle(color=ft.colors.BLACK),
            ),
        ],
        spacing=5,
        horizontal_alignment=ft.CrossAxisAlignment.START,
    )

    senha = ft.Column(
        controls=[ 
            ft.Text("Senha", size=16, weight="w600", color=ft.colors.WHITE),
            ft.TextField(
                label=None,
                hint_text="Digite sua senha",
                bgcolor=ft.colors.WHITE,
                border_color=ft.colors.BLACK,
                border_width=1,
                width=200,
                height=40,
                password=True,
                text_style=ft.TextStyle(color=ft.colors.BLACK),
            ),
        ],
        spacing=5,
        horizontal_alignment=ft.CrossAxisAlignment.START,
    )

    esqueci_senha = ft.TextButton(
        text="Esqueceu sua senha?",
        style=ft.ButtonStyle(
            color=ft.colors.BLACK,
        ),
        content=ft.Text(
            value="Esqueceu sua senha?",
            size=11,
            weight="w600",
            color=ft.colors.BLACK,
        ),
        on_click=lambda e: page.add(ft.Text("Redirecionando para página de recuperação..."))
    )

    registro = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.Text("Não tem uma conta?", size=14, weight="w600", color=ft.colors.BLACK),
                    ft.TextButton(
                        text="Registrar agora",
                        style=ft.ButtonStyle(
                            color=ft.colors.GREY
                        ),
                        on_click=lambda e: page.add(ft.Text("Redirecionando para a página de cadastro...")),
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=5,
            ),
        ],
        width=250,
        height=13,
        scale=0.9,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    google = ft.Container(
        width=207,
        height=40,
        bgcolor=ft.colors.WHITE,
        border_radius=10,
        content=ft.Row(
            controls=[
                ft.Image(src="https://imgs.search.brave.com/xj-TV7sqj2Dzi76ov-9LZ-vSQ6x0UYbHi3RFyXksBSY/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9zdGF0/aWMtMDAuaWNvbmR1/Y2suY29tL2Fzc2V0/cy4wMC9nb29nbGUt/aWNvbi0yMDQ4eDIw/NDgtY3puM2c4eDgu/cG5n", width=20, height=20),
                ft.Text("Google", size=16, weight="w400", color=ft.colors.RED)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
        ),
        on_click=lambda e: page.add(ft.Text("Você clicou no Google!")),
    )

    facebook = ft.Container(
        width=207,
        height=40,
        bgcolor=ft.colors.WHITE,
        border_radius=10,
        content=ft.Row(
            controls=[
                ft.Icon(name="Facebook", color=ft.colors.BLUE),
                ft.Text("Facebook", size=16, weight="w400", color=ft.colors.BLUE)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
        ),
        on_click=lambda e: page.add(ft.Text("Você clicou no Facebook!")),
    )

    play_button = ft.Container(
        width=136,
        height=37,
        border_radius=25,
        bgcolor=ft.colors.GREEN,
        content=ft.Icon(
            name=ft.icons.PLAY_ARROW,
            color=ft.colors.BLACK,
            size=40,
        ),
        alignment=ft.alignment.center,
    )

    formulario = ft.Container(
        content=ft.Column(
            controls=[ 
                email,
                senha,
                esqueci_senha,
                registro,
                google,
                facebook,
                play_button,  # Botão "play" adicionado aqui
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        ),
        top=80,
        width=270,
    )

    stack.controls.append(first_bg)
    stack.controls.append(second_bg)
    stack.controls.append(formulario)
    stack.controls.append(login)

    page.add(stack)

ft.app(target=main)
