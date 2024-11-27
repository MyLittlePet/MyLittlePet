import flet as ft

def main(page: ft.Page):
   
    page.title = "Cadastro"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

   
    background = ft.Stack(
        [
          
            ft.Container(
                width=287.38,
                height=585,
                bgcolor="#FFDD78",
            ),
           
            ft.Container(
                width=246,
                height=500,
                bgcolor="#C2690A",
                left=(287.38 - 246) / 2, 
                top=(585 - 500) / 2,    
            ),
            
            ft.Container(
                content=ft.ElevatedButton(
                    text="Sou Pai/Mãe de Pet",
                    width=190,
                    height=70, 
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=25),
                        text_style=ft.TextStyle(
                            size=24,
                            weight="w400", 
                            
                        ),    
                    ),
                    bgcolor=ft.colors.GREEN,
                    color=ft.colors.WHITE,
                    
                ),
                left=(287.38 - 246) / 2 + (246 - 200) / 2,
                top=(585 - 500) / 2 + 168,     
            ),
            
            ft.Container(
                content=ft.ElevatedButton(
                    text="Estou aqui para os pets",
                    width=190,
                    height=70   ,  
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=25),
                        text_style=ft.TextStyle(
                            size=25.5,
                            weight="w400", 
                        ),                      
                    ),
                    color=ft.colors.WHITE,
                    bgcolor=ft.colors.GREEN,
                    
                ),
                left=(287.38 - 246) / 2 + (246 - 200) / 2, 
                top=(585 - 500) / 2 + 328,    
            ),
        ]
    )

    
    page.add(background)

ft.app(target=main)
