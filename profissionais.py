import flet as ft

def create_schedule_item(name, valor, nota, image_url):
    return ft.Container(
        content=ft.Row(
            [
                # Imagem de perfil
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
                # Informações do agendamento (nome, valor e nota)
                ft.Column(
                    [
                        ft.Text(name, size=16, weight=ft.FontWeight.BOLD, color="black"),
                        # Exibir valor e nota na mesma linha
                        ft.Row(
                            [
                                ft.Text(f"R$ {valor}", size=14, color="#7D7D7D"),
                                ft.Text(" • ", size=14, color="#7D7D7D"),  # Separador
                                ft.Text(f"Nota: {nota} ⭐", size=14, color="#6A6A6A"),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            spacing=5,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    spacing=5,
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=15,  # Espaçamento entre a imagem e as informações
        ),
        padding=10,
        bgcolor="#F4E3D7",
        border_radius=10,
        margin=ft.margin.symmetric(vertical=5, horizontal=10),
    )

def main(page: ft.Page):
    page.title = "Profissionais"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START  # Inicia no topo
    page.padding = 0
    page.bgcolor = '#FFDD78'
    page.window_width = 287.38
    page.window_height = 585

    # Header com ícone e título
    header = ft.Container( 
        content=ft.Row(
            [
                ft.Icon(ft.icons.ARROW_BACK, color="black", size=30),
                ft.Container(
                    content=ft.Text(
                        "Profissionais",
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

    # Lista de agendamentos com fotos (horarios)
    horarios = [
        {"name": "Mateus Emiliano", "valor": "100", "nota": "4.9", "image_url": "https://i.pinimg.com/736x/fe/e6/01/fee6011fbd468bd46d2dfab5d4551cac.jpg"},
        {"name": "Marcos Ribeiro", "valor": "120", "nota": "4.8", "image_url": "https://i.pinimg.com/736x/70/80/8d/70808dc7d62d425dbf93b44b7ea8b6ac.jpg"},
        {"name": "Julia Martins", "valor": "150", "nota": "4.7", "image_url": "https://i.pinimg.com/736x/56/c0/3d/56c03da68f361d79db82d0ff037ce1e1.jpg"},
        {"name": "Maria dos Santos", "valor": "90", "nota": "5.0", "image_url": "https://i.pinimg.com/736x/0f/cc/26/0fcc2683940ed39fb786bf43ccd06d63.jpg"}
    ]

    schedule_container = ft.Container(
        content=ft.Column(
            [
                create_schedule_item(horario["name"], horario["valor"], horario["nota"], horario["image_url"]) 
                for horario in horarios
            ],
            spacing=10,  # Maior espaçamento entre os itens
        ),
        bgcolor="#73513D",  # Fundo marrom atrás dos cards
        border_radius=20,
        padding=ft.Padding(top=10, bottom=60, left=10, right=10),
        margin=ft.margin.only(top=10, bottom=0, left=0, right=0),  # Corrigido para o uso de "only"
    )

    # Estrutura de layout da página (header + cards)
    page.add(
        ft.Column(
            controls=[
                header,  # Adiciona o header no topo
                schedule_container  # Adiciona os cards abaixo do header
            ],
            spacing=10,  # Espaçamento entre os cards
            scroll="auto",  # Rolagem automática se necessário
        ),
    )

    # Barra de navegação (não é o foco, mas incluída no código)
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.HOME_ROUNDED, label="Tela Inicial"),
            ft.NavigationBarDestination(icon=ft.icons.PERSON_ROUNDED, label="Perfil"),
        ],
        bgcolor='#BF5F0B',
        indicator_color='#DE8A18'
    )

    page.update()

# Executa o aplicativo
ft.app(target=main)




