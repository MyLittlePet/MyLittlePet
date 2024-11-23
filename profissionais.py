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
                        bgcolor="#8C5120",
                    ),
                    padding=ft.padding.only(left=20, right=20, top=10, bottom=10),  # Adiciona padding ao redor do texto
                    bgcolor="#8C5120",  # Fundo do texto
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
        {"name": "Mateus Emiliano", "valor": "100", "nota": "4.9", "image_url": "https://i.pinimg.com/736x/5a/be/3b/5abe3b7f37eee1519937b8923be6ecfc.jpg"},
        {"name": "Marcos Ribeiro", "valor": "120", "nota": "4.8", "image_url": "https://i.pinimg.com/736x/32/a5/b8/32a5b84575fc64b48f10a0db8b1b47d4.jpg"},
        {"name": "Julia Martins", "valor": "150", "nota": "4.7", "image_url": "https://i.pinimg.com/736x/f2/35/0d/f2350d28902a31c70b748f6c83c555f6.jpg"},
        {"name": "Maria dos Santos", "valor": "90", "nota": "5.0", "image_url": "https://i.pinimg.com/736x/64/dd/e1/64dde1ba44c0b2488704222b14b60612.jpg"}
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




