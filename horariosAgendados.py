import flet as ft

def main(page: ft.Page):
    page.title = "Horários Agendados"
    page.bgcolor = '#FFDD78'
    page.padding = 0  
    page.scroll = ft.ScrollMode.ALWAYS
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 287.38
    page.window_height = 585

    # Header da Página
    header = ft.Container(
        content=ft.Row(
            [
                ft.Icon(ft.icons.ARROW_BACK, color="black", size=30),
                ft.Container(
                    content=ft.Text(
                        "Horários Agendados",
                        weight=ft.FontWeight.BOLD,
                        color='white',
                        text_align='center',
                        size=15,
                        bgcolor="#D4A373",
                    ),
                    padding=ft.padding.only(left=20, right=20, top=10, bottom=10),  # Adiciona padding ao redor do texto
                    bgcolor="#D4A373",  # Fundo do texto
                    border_radius=50,  # Arredonda as bordas
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=10,
        height=60,
        bgcolor="#FFDD78",
    )

    # Função para criar cada item de agendamento
    def create_schedule_item(name, date, time, image_url):
        return ft.Container(
            content=ft.Row(
                [
                    # Substituindo o círculo pelo componente de imagem
                    ft.Container(
                        width=50,
                        height=50,
                        content=ft.Image(
                            src=image_url,  # Caminho da imagem
                            fit=ft.ImageFit.COVER,
                        ),
                        border_radius=25,  # Mantendo bordas arredondadas
                        clip_behavior=ft.ClipBehavior.HARD_EDGE,
                    ),
                    ft.Column(
                        [
                            ft.Text(name, size=16, weight=ft.FontWeight.BOLD, color="black"),
                            # Exibir data e hora na mesma linha
                            ft.Row(
                                [
                                    ft.Text(date, size=14, color="#7D7D7D"),
                                    ft.Text(" • ", size=14, color="#7D7D7D"),  # Separador
                                    ft.Text(time, size=14, color="#6A6A6A"),
                                ],
                                alignment=ft.MainAxisAlignment.START,
                                spacing=5,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        spacing=5,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                spacing=15,
            ),
            padding=10,
            bgcolor="#F4E3D7",
            border_radius=10,
            margin=ft.margin.symmetric(vertical=5, horizontal=10),
        )
    # Lista de agendamentos com fotos
    schedule_container = ft.Container(
    content=ft.Column(
        [
            create_schedule_item(
                "Mateus Emiliano", "10/11/2024", "09:30", "https://i.pinimg.com/736x/fe/e6/01/fee6011fbd468bd46d2dfab5d4551cac.jpg"
            ),
            create_schedule_item(
                "Marcos Ribeiro", "25/11/2024", "11:00", "https://i.pinimg.com/736x/70/80/8d/70808dc7d62d425dbf93b44b7ea8b6ac.jpg"
            ),
            create_schedule_item(
                "Julia Martins", "05/12/2024", "15:00", "https://i.pinimg.com/736x/56/c0/3d/56c03da68f361d79db82d0ff037ce1e1.jpg"
            ),
            create_schedule_item(
                "Maria dos Santos", "17/12/2024", "18:30", "https://i.pinimg.com/736x/0f/cc/26/0fcc2683940ed39fb786bf43ccd06d63.jpg"
            ),
        ],
        spacing=10,  # Maior espaçamento entre os itens
    ),
    bgcolor="#73513D",  # Fundo marrom atrás dos cards
    border_radius=20,
    padding=ft.Padding(top=10, bottom=50, left=10, right=10),
    margin=ft.margin.only(top=10, bottom=0, left=0, right=0),  # Corrigido para o uso de "only"
)

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
    page.add(header, schedule_container)
    page.update()

# Executar o app
ft.app(target=main)

