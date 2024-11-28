import flet as ft

def main(page: ft.Page):
    page.title = "Tela Inicial"
    page.bgcolor = '#FFDD78'
    page.padding = 0  
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.width = 287.38
    page.window.height = 585

    header = ft.Container(
        content=ft.Row(
            [
                ft.Container(
                    content=ft.Text(
                        "Tela Inicial",
                        weight=ft.FontWeight.BOLD,
                        color='white',
                        text_align='center',
                        size=15,
                        bgcolor="#8C5120",
                    ),
                    padding=ft.padding.only(left=20, right=20, top=10, bottom=10), 
                    bgcolor="#8C5120",
                    border_radius=50,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=10,
        height=60,
        bgcolor="#FFDD78",
    )

    # Diminuindo a altura do background do meio
    middle_background = ft.Container(
        bgcolor="#73513D",
        width=287.38,
        height=450,  # Alterando a altura para 450
        border_radius=20,
    )

    button1 = ft.ElevatedButton(
        text="Ver Serviços Agendados",
        width=200,
        height=80,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=25),
            bgcolor="#779030",
            text_style=ft.TextStyle(
                weight=ft.FontWeight.W_400,
                size=24,
                color="#FFFFFF"
            ),
        ),
        on_click=None,
    )

    button2 = ft.ElevatedButton(
        text="Ver Horários Agendados",
        width=200,
        height=80,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=25),
            bgcolor="#779030",
            text_style=ft.TextStyle(
                weight=ft.FontWeight.W_400,
                size=24,
                color="#FFFFFF"
            ),
        ),
        on_click=None,
    )

    button3 = ft.ElevatedButton(
        text="Contrate Um Serviço",
        width=200,
        height=80,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=25),
            bgcolor="#779030",
            text_style=ft.TextStyle(
                weight=ft.FontWeight.W_400,
                size=24,
                color="#FFFFFF"
            ),
        ),
        on_click=None,
    )

    middle_container = ft.Container(
        content=ft.Stack(
            controls=[
                middle_background,
                ft.Container(
                    content=ft.Column(
                        controls=[button1, button2, button3],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=40,
                    ),
                    alignment=ft.Alignment(0, 0),
                    height=380,
                    width=250,
                ),
            ]
        ),
        width=287.38,
        height=585,
    )

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.HOME_ROUNDED, label="Tela Inicial"),
            ft.NavigationBarDestination(icon=ft.icons.PERSON_ROUNDED, label="Perfil"),
        ],
        bgcolor="#BF5F0B",
        indicator_color="#DE8A18",
    )

    page.add(header, middle_container)
    page.update()

ft.app(target=main)
