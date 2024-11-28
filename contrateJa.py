import flet as ft

def main(page: ft.Page):
    page.title = "Tela de Cadastro"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 10
    page.bgcolor = '#FFDD78'
    page.window_width = 287.38
    page.window_height = 585

    # Função para ser executada ao clicar no botão de pesquisa
    def pesquisar(e):
        horario = horario_field.value
        avaliacao = avaliacao_field.value
        tipo_pet = tipo_pet_field.value
        valor_hora = valor_hora_field.value
        # Exibir os dados coletados
        page.dialog = ft.AlertDialog(
            title=ft.Text("Dados da Pesquisa"),
            content=ft.Text(f"Horário: {horario}\nAvaliação: {avaliacao}\nTipo de Pet: {tipo_pet}\nValor por Hora: {valor_hora}"),
            on_dismiss=lambda e: print("Diálogo fechado")
        )
        page.dialog.open = True
        page.update()

    # Campos de texto do formulário
    horario_field = ft.TextField(label="Horário", border_radius=15, filled=True, bgcolor="#DAD8DB", color="black")
    avaliacao_field = ft.TextField(label="Avaliação", border_radius=15, filled=True, bgcolor="#DAD8DB", color="black")
    tipo_pet_field = ft.TextField(label="Tipo de pet", border_radius=15, filled=True, bgcolor="#DAD8DB", color="black")
    valor_hora_field = ft.TextField(label="Valor por hora", border_radius=15, filled=True, bgcolor="#DAD8DB", color="black")

    # Container principal do aplicativo
    main_container = ft.Container(
        width=300,
        padding=ft.padding.all(10),
        border_radius=20,
        bgcolor="#FFE29F",
        content=ft.Column(
            [
                # Botão de contratar
                ft.Container(
                    content=ft.Text("Contrate já!", color="white", size=18, weight="bold"),
                    bgcolor="#8B4513",
                    padding=ft.padding.symmetric(horizontal=30, vertical=10),
                    border_radius=20,
                    alignment=ft.alignment.center,
                ),
                
                # Seção de filtros
                ft.Container(
                    margin=ft.margin.only(top=10),
                    padding=20,
                    border_radius=20,
                    bgcolor="#A0522D",
                    content=ft.Column(
                        [
                            ft.Text("Filtros de busca", color="white", size=18, weight="bold"),
                            ft.Container(content=horario_field, border_radius=15, margin=ft.margin.only(top=10)),
                            ft.Container(content=avaliacao_field, border_radius=15, margin=ft.margin.only(top=10)),
                            ft.Container(content=tipo_pet_field, border_radius=15, margin=ft.margin.only(top=10)),
                            ft.Container(content=valor_hora_field, border_radius=15, margin=ft.margin.only(top=10)),
                            ft.IconButton(
                                icon=ft.icons.SEARCH,
                                icon_color="white",
                                bgcolor="#8B4513",
                                icon_size=20,
                                padding=10,
                                alignment=ft.alignment.center,
                                on_click=pesquisar,  # Ação do botão de pesquisa
                            ),
                        ],
                        spacing=10,
                    ),
                ),
            ],
            spacing=15,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )

    # Adiciona o container principal à página
    page.add(main_container)

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
