import flet as ft
from views.home_view import HomeView # [NUEVO]

def main(page: ft.Page):
    page.title = "🎞️ Flet Películas"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.BLUE_GREY_900
    page.padding = 20
    
    # [MODIFICADO] Ahora simplemente cargamos la vista que creamos
    page.add(HomeView(page))

if __name__ == "__main__":
    ft.run(main)