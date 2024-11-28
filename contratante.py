import flet as ft

def main(page: ft.Page):
    page.title = "Tela de Cadastro"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = 10
    page.bgcolor = '#FFDD78'
    page.window_width = 287.38
    page.window_height = 585
    
    def cadastrar(e):
        if not nome_input.value or not registro_input.value or not senha_input.value:
            msg.value = "Por favor, preencha todos os campos."
            page.update()
            return
        msg.value = f"Cadastro realizado com sucesso! Bem-vindo, {nome_input.value}!"
        nome_input.value = ""
        registro_input.value = ""
        senha_input.value = ""
        tipoPet_input.value = None
        banco_input.value = ""
        agencia_input.value = ""
        conta_input.value = ""
        page.update()
    
    tipoPet_input = ft.Dropdown(
        label="Tipo de Pet",
        icon_enabled_color='black',
        options=[
            ft.dropdown.Option("Cão"),
            ft.dropdown.Option("Gato"),
        ],
        width=300,
        height=40, 
        bgcolor='#F0F0F0',
        color='black',
    )
    
    # Título da tela
    titulo = ft.Container(
        content=ft.Text(
            "Sou Contratante",
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

    dadosBanco = ft.Container(
        content=ft.Text(
            "Dados bancários:",
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
    
    # Campos de entrada
    nome_input = ft.TextField(label="Nome Completo", width=400, height=40, label_style=ft.TextStyle(color='#B0B0B0'), bgcolor='#F0F0F0', content_padding=ft.Padding(top=10, right=10, bottom=10, left=10))
    registro_input = ft.TextField(label="RG", width=400, height=40, label_style=ft.TextStyle(color='#B0B0B0'), bgcolor='#F0F0F0', content_padding=ft.Padding(top=10, right=10, bottom=10, left=10))
    senha_input = ft.TextField(label="Senha", password=True, height=40, can_reveal_password=True, width=400, label_style=ft.TextStyle(color='#B0B0B0'), bgcolor='#F0F0F0', content_padding=ft.Padding(top=10, right=10, bottom=10, left=10))
    
    #dados bancários
    banco_input = ft.TextField(label="Número do banco", width=400, height=40, label_style=ft.TextStyle(color='#B0B0B0'), bgcolor='#F0F0F0', content_padding=ft.Padding(top=10, right=10, bottom=10, left=10))
    agencia_input = ft.TextField(label="Agência", width=400, height=40, label_style=ft.TextStyle(color='#B0B0B0'), bgcolor='#F0F0F0', content_padding=ft.Padding(top=10, right=10, bottom=10, left=10))
    conta_input = ft.TextField(label="Conta", width=400, height=40, label_style=ft.TextStyle(color='#B0B0B0'), bgcolor='#F0F0F0', content_padding=ft.Padding(top=10, right=10, bottom=10, left=10))
    
    # Botão de "play"
    cadastrar_button = ft.ElevatedButton(
    content=ft.Row(
        [
            ft.Icon(ft.icons.PLAY_ARROW_ROUNDED, size=40)  # Ajuste o tamanho do ícone conforme necessário
        ],
        alignment=ft.MainAxisAlignment.CENTER  # Alinha o ícone no centro do botão
    ),
    on_click=cadastrar,
    text=" ",
    width=100,
    height=40,
    bgcolor='#788C30',
    color='#232624'
)
    
    # Mensagem de confirmação
    msg = ft.Text("", color=ft.colors.GREEN)
    
    #clique
    login_row = ft.Row(
        controls=[
            ft.Text("Já tem uma conta?", color=ft.colors.BLACK),
            ft.GestureDetector(
                content=ft.Text("Logar", color=ft.colors.BLUE, weight=ft.FontWeight.BOLD),
                on_tap=lambda e: print("Login clicado"),
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )
    
    #componentes na página
    formulario_container = ft.Container(
        content=ft.Column(
            [
                titulo,
                nome_input,
                registro_input,
                tipoPet_input,
                dadosBanco,
                banco_input,
                agencia_input,
                conta_input,
                login_row,
                cadastrar_button,
                msg
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        ),
        width=260,
        padding=18,
        bgcolor="#BF5F0B",
        border_radius=20,
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=10,
            color=ft.colors.BLACK12,
            offset=ft.Offset(4, 4),
        ),
        alignment=ft.alignment.center
    )
    
    # Adiciona o container laranja na página
    page.add(formulario_container)

ft.app(target=main)




