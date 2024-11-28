import flet as ft

def main(page: ft.Page):
    # Configurações iniciais da página
    page.title = "Detalhes do Prestador"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = 0
    page.bgcolor = '#FFDD78'
    page.window_width = 287.38
    page.window_height = 585

    # Função de navegação
    def navigate_to(screen):
        if screen == "Tela Inicial":
            page.snack_bar = ft.SnackBar(ft.Text("Navegando para Tela Inicial!"))
        elif screen == "Perfil":
            page.snack_bar = ft.SnackBar(ft.Text("Navegando para Perfil!"))
        page.snack_bar.open()

    # Callback da barra de navegação
    def on_navigation_change(event):
        navigate_to(event.control.label)

    # Barra de navegação
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.HOME_ROUNDED, label="Tela Inicial"),
            ft.NavigationBarDestination(icon=ft.icons.PERSON_ROUNDED, label="Perfil"),
        ],
        bgcolor="#BF5F0B",
        indicator_color="#DE8A18",
        on_change=on_navigation_change,  # Vincula a navegação
    )

    # Função para iniciar o chat
    def iniciar_chat(e):
        page.dialog = ft.AlertDialog(
            title=ft.Text("Chat Iniciado"),
            content=ft.Text("Você iniciou um chat com Mateus Emiliano Soares."),
            actions=[
                ft.TextButton(
                    "Fechar",
                    on_click=lambda e: page.dialog.close(),
                )
            ],
        )
        page.dialog.open()

    # Cabeçalho com ícone
    header = ft.Container(
        content=ft.Row(
            [
                ft.Icon(ft.icons.ARROW_BACK, color="black", size=30),  # Ícone de voltar
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=10,
        height=60,
        bgcolor="#FFDD78",  # Fundo do cabeçalho
    )

    # Conteúdo do cartão principal
    card = ft.Container(
        content=ft.Column(
            [
                # Foto de perfil
                ft.Container(
                    content=ft.Image(
                        src="https://i.pinimg.com/736x/b4/8b/9a/b48b9a62d1414fa9cd865ca1c3519cfb.jpg",  # URL da foto de perfil
                        fit=ft.ImageFit.COVER,
                        width=100,
                        height=100,
                        border_radius=ft.border_radius.all(50),  # Torna a imagem redonda
                    ),
                    alignment=ft.alignment.center,
                    padding=ft.padding.all(10),
                ),
                # Nome do prestador centralizado
                ft.Container(
                    content=ft.Text(
                        "Mateus Emiliano Soares",
                        weight=ft.FontWeight.BOLD,
                        size=18,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    alignment=ft.alignment.center,
                ),
                # Valor por hora centralizado
                ft.Container(
                    content=ft.Text(
                        "Valor por Hora: R$100",
                        size=16,
                        text_align=ft.TextAlign.CENTER,
                        color="black",
                    ),
                    alignment=ft.alignment.center,
                ),
                # Avaliação
                ft.Row(
                    [
                        ft.Icon(ft.icons.STAR, color="gold", size=20),
                        ft.Text(
                            "4.9",
                            size=16,
                            color="black",
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=5,
                ),
                # Botão "Iniciar Chat" centralizado
                ft.Container(
                    content=ft.ElevatedButton(
                        text="Iniciar Chat",
                        icon=ft.icons.CHAT,
                        bgcolor="#7F8C4F",
                        color="white",
                        on_click=iniciar_chat,
                    ),
                    alignment=ft.alignment.center,  # Centraliza o botão
                    margin=ft.margin.only(top=10),  # Margem superior para separação
                ),
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        alignment=ft.alignment.center,
        bgcolor="#DFAE21",
        padding=ft.padding.all(20),
        border_radius=ft.border_radius.all(15),
    )

    # Fundo marrom ao redor do cartão principal
    card_container = ft.Container(
        content=card,
        bgcolor="#73513D",  # Fundo marrom
        border_radius=20,  # Bordas arredondadas
        padding=ft.Padding(top=10, bottom=60, left=10, right=10),  # Padding para espaçamento interno
        margin=ft.margin.only(top=10),  # Margem superior para separar o fundo do cabeçalho
    )

    # Adiciona os widgets na página
    page.add(
        header,  # Adiciona o cabeçalho personalizado
        card_container,  # Adiciona o fundo marrom ao redor do cartão
    )

ft.app(target=main)
