import flet as ft

def main(page: ft.Page):
    # Configuração inicial
    page.title = "Horários Agendados"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#F0D68C"
    page.window_width = 287.38
    page.window_height = 585
    
    # Lista de horários (dados)
    horarios = [
        {"nome": "Mateus Emiliano Soares", "valor": 100, "turno": "Diurno", "nota": 4.9, "foto": "https://i.pinimg.com/736x/5a/be/3b/5abe3b7f37eee1519937b8923be6ecfc.jpg"},
        {"nome": "Marcos Ribeiro Da Silva", "valor": 120, "turno": "Noturno", "nota": 4.8, "foto": "https://i.pinimg.com/736x/32/a5/b8/32a5b84575fc64b48f10a0db8b1b47d4.jpg"},
        {"nome": "Julia Martins Azevedo", "valor": 150, "turno": "Diurno", "nota": 4.7, "foto": "https://i.pinimg.com/736x/f2/35/0d/f2350d28902a31c70b748f6c83c555f6.jpg"},
        {"nome": "Maria Dos Santos", "valor": 90, "turno": "Noturno", "nota": 5.0, "foto": "https://i.pinimg.com/736x/64/dd/e1/64dde1ba44c0b2488704222b14b60612.jpg"},
    ]

    # Função para criar os cards de horários
    def criar_card(horario):
        return ft.Card(
        elevation=2,
        content=ft.GestureDetector(
            on_tap=lambda e, horario=horario: None,  # Não faz nada ao clicar
            content=ft.Container(
                content=ft.Row(
                    controls=[
                        # Foto de perfil 
                        ft.CircleAvatar(
    radius=20, 
    foreground_image_url=horario["foto"],  
),

                        # Coluna com o nome, valor e turno
                        ft.Column(
                            controls=[
                                # Nome
                                ft.Text(
                                    horario["nome"],
                                    size=16,
                                    weight="bold",
                                    color="#D9D9D9",
                                ),
                                # Valor e turno
                                ft.Text(
                                    f"R$ {horario['valor']} - {horario['turno']}",
                                    size=14,
                                    color="#D9D9D9",
                                ),
                                # Nota
                                ft.Text(
                                    f"Nota: {horario['nota']} ⭐",
                                    size=14,
                                    color="#D9D9D9",
                                ),
                            ],
                            spacing=5,
                        ),
                    ],
                    spacing=10, 
                ),
                padding=10,
                bgcolor="#D8AA20",
                border_radius=10,
                width=300,  
            ),
        ),
    )

    titulo = ft.Container(
        content=ft.Text(
            "Horários Agendados",
            weight=ft.FontWeight.BOLD,
            color='white',
            text_align='center',
            size=15
        ),
        bgcolor='#788C30',
        width=150,
        border_radius=25, 
        height=40, 
        padding=ft.Padding(top=10, right=10, bottom=10, left=10)
    )

    # Tela com o título e os cards
    page.add(
        titulo,  # Adiciona o título no topo
        ft.Column(
            controls=[criar_card(horario) for horario in horarios],
            spacing=10,
            scroll="auto",
        ),
    )

    # Barra de navegação
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.HOME_ROUNDED, label="Tela Inicial"),
            ft.NavigationBarDestination(icon=ft.icons.PERSON_ROUNDED, label="Perfil"),
        ],
        bgcolor='#BF5F0B',
        indicator_color='#DE8A18'
    )

    page.update()  

ft.app(target=main)








