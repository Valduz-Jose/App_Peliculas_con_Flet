import flet as ft
from services.pelicula_service import PeliculaService

def HomeView(page: ft.Page):
    # Título
    titulo = ft.Row(
        controls=[
            ft.Icon(ft.Icons.MOVIE, size=30, color=ft.Colors.AMBER),
            ft.Text("Catálogo de Películas", size=24, weight=ft.FontWeight.BOLD)
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    # Tabla
    tabla = ft.DataTable(
        expand=True,
        border=ft.border.all(1, ft.Colors.BLUE_GREY_700),
        border_radius=10,
        heading_row_color=ft.Colors.BLUE_GREY_800,
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Título")),
            ft.DataColumn(ft.Text("Director")),
            ft.DataColumn(ft.Text("Puntuación")),
            ft.DataColumn(ft.Text("Acciones")), # Columna para futuros botones
        ],
    )

    def cargar_datos():
        peliculas = PeliculaService.obtener_todos()
        tabla.rows.clear()
        for peli in peliculas:
            tabla.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(peli.id))),
                        ft.DataCell(ft.Text(peli.titulo)),
                        ft.DataCell(ft.Text(peli.director)),
                        ft.DataCell(ft.Text(str(peli.puntuacion))),
                        ft.DataCell(ft.Row([ft.IconButton(ft.Icons.EDIT, icon_color=ft.Colors.BLUE_400)]))
                    ]
                )
            )
        page.update()

    # Contenedor principal de la vista
    content = ft.Column(
        controls=[
            titulo,
            ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
            ft.Column([tabla], scroll=ft.ScrollMode.ADAPTIVE, expand=True)
        ],
        expand=True
    )

    # Cargamos los datos inicialmente
    cargar_datos()
    
    return content