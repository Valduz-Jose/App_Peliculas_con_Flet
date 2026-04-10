import flet as ft

def main(page: ft.Page):
    # Configuración de la página
    page.title = "🎞️ Flet Películas"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.BLUE_GREY_900
    
    # Alineación centrada para el contenido
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Contenedor principal adaptable
    contenido = ft.Column(
        controls=[
            # [MODIFICADO] Se eliminó 'name=' ya que el primer argumento es el icono
            ft.Icon(ft.Icons.MOVIE, size=50, color=ft.Colors.AMBER), 
            ft.Text(
                "Bienvenido al Sistema de Películas",
                size=30,
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Text(
                "Tu primera app CRUD con Flet y MySQL",
                size=16,
                color=ft.Colors.BLUE_GREY_200,
                text_align=ft.TextAlign.CENTER
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
    )

    page.add(contenido)

if __name__ == "__main__":
    # [MODIFICADO] Se cambió ft.app por ft.run para evitar el aviso de desuso
    ft.run(main)