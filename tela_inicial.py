import flet as ft

def main(page: ft.Page):
    page.title = "Tela Inicial"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    stack = ft.Stack(
        width=293,
        height=585,
    )

    first_bg = ft.Container(
        width=293,
        height=585,
        border_radius=20,
        bgcolor="#FFDD78",
    )

    second_bg = ft.Container(
        width=293,
        height=456,
        border_radius=15,
        bgcolor="#7D5D42",
    )
    second_bg.top = 126

    third_bg = ft.Container(
        width=293,
        height=58,
        border_radius=20,
        bgcolor="#D0802B",
    )
    third_bg.top = 534

    avatar = ft.CircleAvatar(
        foreground_image_url="https://i.postimg.cc/pTCt4Mwv/Blue-Modern-Minimal-Pet-Clinic-Logo-3.png",
        width=50,
        height=50,
    )
    avatar.top = 16
    avatar.left = (293 - 50) // 2

    inicio_texto = ft.Container(
        width=231,
        height=31,
        border_radius=9,
        bgcolor=ft.colors.BROWN,
        content=ft.Text(
            "Tela Inicial",
            size=16,
            weight=ft.FontWeight.W_600,
            color=ft.colors.WHITE,
        ),
        alignment=ft.alignment.center,
    )
    inicio_texto.top = 77
    inicio_texto.left = 31

    def on_button_click(e):
        page.dialog = ft.AlertDialog(title=ft.Text(f"Você clicou no botão: {e.control.data}"))
        page.dialog.open = True
        page.update()

    second_bg_top = 126
    second_bg_height = 456
    button_height = 80
    button_spacing = (second_bg_height - (3 * button_height)) // 4

    botao_servicos = ft.Container(
        width=200,
        height=button_height,
        border_radius=25,
        bgcolor='#779030',
        content=ft.Text(
            "Ver Serviços Agendados",
            size=16,
            weight=ft.FontWeight.W_400,
            color=ft.colors.WHITE,
            text_align=ft.TextAlign.CENTER,
        ),
        alignment=ft.alignment.center,
        data="Serviços",
        on_click=on_button_click,
    )
    botao_servicos.top = second_bg_top + button_spacing
    botao_servicos.left = (293 - 200) // 2

    botao_horario = ft.Container(
        width=200,
        height=button_height,
        border_radius=25,
        bgcolor='#779030',
        content=ft.Text(
            "Ver Horários Agendados",
            size=16,
            weight=ft.FontWeight.W_400,
            color=ft.colors.WHITE,
            text_align=ft.TextAlign.CENTER,
        ),
        alignment=ft.alignment.center,
        data="Horários",
        on_click=on_button_click,
    )
    botao_horario.top = botao_servicos.top + button_height + button_spacing
    botao_horario.left = (293 - 200) // 2

    botao_contratar = ft.Container(
        width=200,
        height=button_height,
        border_radius=25,
        bgcolor='#779030',
        content=ft.Text(
            "Contrate um serviço",
            size=16,
            weight=ft.FontWeight.W_400,
            color=ft.colors.WHITE,
            text_align=ft.TextAlign.CENTER,
        ),
        alignment=ft.alignment.center,
        data="Contratar",
        on_click=on_button_click,
    )
    botao_contratar.top = botao_horario.top + button_height + button_spacing
    botao_contratar.left = (293 - 200) // 2

    botao_tela_inicial = ft.Container(
        width=63,
        height=44,
        content=ft.Column(
            controls=[
                ft.Icon(ft.icons.HOME, size=25, color=ft.colors.BLACK),
                ft.Text("Tela Inicial", size=12, color=ft.colors.BLACK, text_align=ft.TextAlign.CENTER),
            ],
            spacing=1,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        alignment=ft.alignment.center,
        data="Tela Inicial",
        on_click=on_button_click,
    )
    botao_tela_inicial.top = 541
    botao_tela_inicial.left = 58

    botao_perfil = ft.Container(
        width=63,
        height=44,
        content=ft.Column(
            controls=[
                ft.Icon(ft.icons.PERSON_ROUNDED, size=24, color=ft.colors.BLACK),
                ft.Text("Perfil", size=12, color=ft.colors.BLACK, text_align=ft.TextAlign.CENTER),
            ],
            spacing=1,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        alignment=ft.alignment.center,
        data="Perfil",
        on_click=on_button_click,
    )
    botao_perfil.top = 541
    botao_perfil.left = 172

    stack.controls.extend([
        first_bg, second_bg, third_bg, avatar, inicio_texto,
        botao_servicos, botao_horario, botao_contratar, botao_tela_inicial, botao_perfil
    ])

    page.add(stack)

ft.app(target=main)
