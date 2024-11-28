import flet as ft

def main(page: ft.Page):
    page.title = "Contratado"
    page.bgcolor = "#FFDD78"

    page.window.width = 287
    page.window.height = 585

    background = ft.Container(
        width=287,
        height=585,
        bgcolor="#FFDD78",
    )

    segundo_bg = ft.Container(
        width=253.77,
        height=505,
        bgcolor="#C2690A",
    )

 
    botao_contratado = ft.ElevatedButton(
        text="Sou contratado",
        width=200,
        height=40,
        bgcolor="#4CAF50",
        color="white",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=20)
        ),
        disabled=True
    )

    botao_container = ft.Container(
        content=botao_contratado,
        alignment=ft.alignment.center,
        top=40,
        left=30,
    )

    texto_nome_completo = ft.Text(
        value="Nome completo:", 
        weight=400,
        size=15,
        color="white"
    )

    texto_container = ft.Container(
        content=texto_nome_completo,
        top=100,
        left=20,
    )

    textfield_nome_completo = ft.TextField(
        width=184.29,
        height=35,
        border=1,
        bgcolor="white",
        color="black"
    )

    textfield_container = ft.Container(
        content=textfield_nome_completo,
        top=130,
        left=20,
    )

    texto_rg = ft.Text(
        value="Registro Geral (RG):", 
        weight=400,
        size=15,
        color="black"
    )

    texto_rg_container = ft.Container(
        content=texto_rg,
        top=170,
        left=20,
    )

    textfield_rg = ft.TextField(
        width=184.29,
        height=35,
        border=1,
        bgcolor="white",
        color="black"
    )

    textfield_rg_container = ft.Container(
        content=textfield_rg,
        top=200,
        left=20,
    )

    texto_servicos_gerais = ft.Text(
        value="Serviços gerais:", 
        weight=400,
        size=15,
        color="black"
    )

    texto_servicos_container = ft.Container(
        content=texto_servicos_gerais,
        top=240,
        left=20,
    )

    dropdown_servicos = ft.Dropdown(
        width=184.29,
        height=35,
        border=1,
        bgcolor="white",
        color="black",
        options=[ 
            ft.dropdown.Option("Banho e Tosa"),
            ft.dropdown.Option("Vacinação"),
            ft.dropdown.Option("Consulta Veterinária"),
            ft.dropdown.Option("Hospedagem"),
            ft.dropdown.Option("Adestramento"),
            ft.dropdown.Option("Transporte de Animais"),
            ft.dropdown.Option("Venda de Rações e Acessórios")
        ],
    )

    dropdown_container = ft.Container(
        content=dropdown_servicos,
        top=270,
        left=20,
    )

    texto_dados_bancarios = ft.Text(
        value="Dados Bancários:", 
        weight=400,
        size=15,
        color="black"
    )

    texto_dados_bancarios_container = ft.Container(
        content=texto_dados_bancarios,
        top=320,
        left=20,
    )

   
    textfield_numero_banco = ft.TextField(
        width=184.29,
        height=35,
        border=1,
        bgcolor="white",
        color="black",
        label="Número do banco"
    )

    textfield_numero_banco_container = ft.Container(
        content=textfield_numero_banco,
        top=350, 
        left=20,
    )

    textfield_agencia = ft.TextField(
        width=184.29,
        height=35,
        border=1,
        bgcolor="white",
        color="black",
        label="Agência"
    )

    textfield_agencia_container = ft.Container(
        content=textfield_agencia,
        top=390,  
        left=20,
    )

    textfield_conta = ft.TextField(
        width=184.29,
        height=35,
        border=1,
        bgcolor="white",
        color="black",
        label="Conta"
    )

    textfield_conta_container = ft.Container(
        content=textfield_conta,
        top=430,
        left=20,
    )

   
    texto_ja_tem_conta = ft.Text(
        value="Já tem uma conta?", 
        weight=400,
        size=11,
        color="black"
    )

    botao_logar = ft.ElevatedButton(
        text="Logar",
        width=85,
        height=30,
        bgcolor="#C2690A",
        color="white",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=20),
            side=ft.BorderSide(1, color="#C2690A"),
        )
    )

    texto_botao_container = ft.Container(
        content=ft.Row(
            controls=[
                texto_ja_tem_conta,
                botao_logar
            ],
            alignment=ft.MainAxisAlignment.START
        ),
        top=470, 
        left=20,
    )

    stack = ft.Stack()

    stack.controls.append(background)
    stack.controls.append(segundo_bg)
    stack.controls.append(botao_container)
    stack.controls.append(texto_container)
    stack.controls.append(textfield_container)
    stack.controls.append(texto_rg_container)
    stack.controls.append(textfield_rg_container)
    stack.controls.append(texto_servicos_container)
    stack.controls.append(dropdown_container)
    stack.controls.append(texto_dados_bancarios_container)
    stack.controls.append(textfield_numero_banco_container)
    stack.controls.append(textfield_agencia_container)
    stack.controls.append(textfield_conta_container)
    stack.controls.append(texto_botao_container)

    page.add(stack)

ft.app(target=main)
