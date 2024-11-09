import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.title = 'MyLittlePet'
    page.bgcolor = '#FFDD78'
    page.window.width = 287.38
    page.window.height = 585525235252


    page.add(
        ft.CircleAvatar(
            foreground_image_src='https://cdn.discordapp.com/attachments/1298422423460511754/1303181366833451098/Blue_Modern_Minimal_Pet_Clinic_Logo_3.png?ex=672ad1b9&is=67298039&hm=7effb8cb1bd9289fd6d61edc87e3e991bf554527a7481b5e3b1f130b29d92abb&',
            width=156,
            height=151
        ),
        ft.CupertinoButton('Login', color='white', bgcolor=ft.colors.BROWN_500, width=200, border_radius=25),
        ft.CupertinoButton('Cadastro', color='white', bgcolor=ft.colors.BROWN_500, width=200, border_radius=25),
        
        ft.Row(
            controls=[
                ft.IconButton(
                    content=ft.Image(src='https://imgs.search.brave.com/OjC5m0OkpLjRASvopjithEHGJLiDL-ixXgDc_tKwxLM/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9kMjlm/aHB3MDY5Y3R0Mi5j/bG91ZGZyb250Lm5l/dC9pY29uL2ltYWdl/LzM4NzY0L3ByZXZp/ZXcuc3Zn', width=30, height=30)
                ),
                ft.IconButton(
                    content=ft.Image(src='https://imgs.search.brave.com/8fmeceQYxPbDanvp_xqlo-5W7_GXFvMb_FJsKX0QVmo/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9zdGF0/aWMtMDAuaWNvbmR1/Y2suY29tL2Fzc2V0/cy4wMC9mYWNlYm9v/ay1pY29uLTUxMng1/MTItc2ViNTQyanUu/cG5n', width=30, height=30)
                ),
                ft.IconButton(
                    content=ft.Image(src='https://imgs.search.brave.com/xj-TV7sqj2Dzi76ov-9LZ-vSQ6x0UYbHi3RFyXksBSY/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9zdGF0/aWMtMDAuaWNvbmR1/Y2suY29tL2Fzc2V0/cy4wMC9nb29nbGUt/aWNvbi0yMDQ4eDIw/NDgtY3puM2c4eDgu/cG5n', width=30, height=30)
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER, 
            spacing=20
        )
    )

    page.update()

ft.app(target=main)