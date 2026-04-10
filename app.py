import flet as ft
from views.home_view import HomeView
from views.form_view import FormView 
from components.navbar import Navbar

def main(page: ft.Page):
    page.title = "🎞️ Flet Películas"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.BLUE_GREY_900
    page.padding = 20

    def cambiar_vista(e):
        index = e.control.selected_index
        page.controls.clear()
        
        page.navigation_bar = nav
        
        if index == 0:
            page.add(HomeView(page))
        elif index == 1:
            # [SOLUCIÓN DEFINITIVA] Usamos el objeto Alignment directamente
            page.add(
                ft.Container(
                    content=FormView(page), 
                    alignment=ft.Alignment(0, 0), # Esto es el centro exacto (x=0, y=0)
                    expand=True
                )
            )
        page.update()

    nav = Navbar(cambiar_vista)
    page.navigation_bar = nav
    page.add(HomeView(page))

if __name__ == "__main__":
    ft.run(main)