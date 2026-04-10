import flet as ft
from views.home_view import HomeView
from views.form_view import FormView
from components.navbar import Navbar

def main(page: ft.Page):
    page.title = "🎞️ Flet Películas"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.BLUE_GREY_900
    page.padding = 20
    
    # Inicializamos nuestro atributo personalizado
    page.id_pelicula_editar = None

    def cambiar_vista(e):
        # Si el usuario hace click en el botón Agregar de la Navbar, reseteamos el modo edición
        if e is not None and e.control == page.navigation_bar and page.navigation_bar.selected_index == 1:
            page.id_pelicula_editar = None

        index = page.navigation_bar.selected_index
        page.controls.clear()
        
        if index == 0:
            page.add(HomeView(page))
        elif index == 1:
            page.add(FormView(page))
        
        page.update()

    # Configurar Navbar
    nav = Navbar(cambiar_vista)
    page.navigation_bar = nav
    
    # Carga Inicial
    page.add(HomeView(page))
    page.update()

if __name__ == "__main__":
    ft.run(main)