import flet as ft

def main(page: ft.Page):
    page.title = "Serviços Agendados"
    page.bgcolor = '#FFDD78'
    page.padding = 0  

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 287
    page.window_height = 585

   
    header = ft.Container(
        content=ft.Row(
            [
               
                ft.IconButton(
                    icon=ft.icons.ARROW_BACK,
                    icon_size=30,
                    on_click=lambda e: None, 
                    icon_color="black"  
                ),
                ft.Container(
                    content=ft.Text(
                        "Serviços Agendados",
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
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=10,
        height=60,
        bgcolor="#FFDD78",
    )

   
    middle_background = ft.Container(
        bgcolor="#73513D",  
        width=287.38,
        height=585,
        border_radius=20,
    )

    # Avatar
    def create_avatar():
        return ft.Container(
            width=61,
            height=61,
            bgcolor="#808080",  
            border_radius=30.5, 
        )

   
    def create_button(text):
        avatar = create_avatar()
        return ft.ElevatedButton(
            width=257, 
            height=74,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=15),
                bgcolor="#779030",
                text_style=ft.TextStyle(
                    weight=ft.FontWeight.W_400,
                    size=20,
                    color="#FFFFFF"
                ),
            ),
            on_click=None,  
            content=ft.Row(  
                [
                    avatar,  
                    ft.Text(  
                        text,  
                        size=15,
                        weight=ft.FontWeight.W_700,  
                        color="#FFFFFF",  
                        text_align=ft.TextAlign.START,  
                        max_lines=1,  
                        overflow=ft.TextOverflow.ELLIPSIS,  
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,  # Alinha o conteúdo à esquerda
                spacing=10,  # Espaçamento entre o avatar e o texto
            ),
        )


    button1 = create_button("Lucas Silva da Costa")
    button2 = create_button("Ana Clara Macedo")
    button3 = create_button("Julia Soares Espinoza")
    button4 = create_button("Luiz Mariano Marcos")

  
    button_container = ft.Column(
        controls=[
            ft.Container(content=button1, padding=ft.padding.all(10)),
            ft.Container(content=button2, padding=ft.padding.all(10)),
            ft.Container(content=button3, padding=ft.padding.all(10)),
            ft.Container(content=button4, padding=ft.padding.all(10)),
        ],
        alignment=ft.MainAxisAlignment.START, 
        spacing=10, 
        expand=True, 
    )

   
    stack = ft.Stack(
        controls=[middle_background, button_container], 
        width=287.38,
        height=585,
    )

   
    button_container.top = -3  # Ajuste para mover os botões para baixo, no segundo background

    # Footer com botões
    page.navigation_bar = ft.NavigationBar(
        destinations=[ 
            ft.NavigationBarDestination(icon=ft.icons.HOME_ROUNDED, label="Tela Inicial"),
            ft.NavigationBarDestination(icon=ft.icons.PERSON_ROUNDED, label="Perfil"),
        ],
        bgcolor="#BF5F0B",
        indicator_color="#DE8A18",
    )

    # Adicionando elementos à página
    page.add(header, stack)
    page.update()

# Executar o app
ft.app(target=main)
