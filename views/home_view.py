import flet as ft
from services.pelicula_service import PeliculaService

def HomeView(page: ft.Page):
    titulo = ft.Row(
        controls=[
            ft.Icon(ft.Icons.MOVIE, size=30, color=ft.Colors.AMBER),
            ft.Text("Catálogo de Películas", size=24, weight=ft.FontWeight.BOLD)
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

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
            ft.DataColumn(ft.Text("Acciones")),
        ],
    )

    def ir_a_editar(id):
        page.session.set("editar_id", id)
        page.navigation_bar.selected_index = 1
        page.navigation_bar.on_change(
            ft.NavigationBarChangeEvent(control=page.navigation_bar, selected_index=1)
        )

    def cargar_datos():
        peliculas = PeliculaService.obtener_todos()
        tabla.rows.clear()
        for peli in peliculas:
            peli_id = peli.id
            tabla.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(peli.id))),
                        ft.DataCell(ft.Text(peli.titulo)),
                        ft.DataCell(ft.Text(peli.director)),
                        ft.DataCell(ft.Text(str(peli.puntuacion))),
                        ft.DataCell(
                            ft.Row([
                                ft.IconButton(
                                    icon=ft.Icons.EDIT,
                                    icon_color=ft.Colors.BLUE_400,
                                    on_click=lambda _, id=peli_id: ir_a_editar(id)
                                )
                            ])
                        )
                    ]
                )
            )
        page.update()

    # ... (al final de HomeView)
    content = ft.Column(
        controls=[
            titulo,
            ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
            ft.Row(
                controls=[tabla],
                alignment=ft.MainAxisAlignment.CENTER, # Centra la tabla en el Row
            )
        ],
        expand=True,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER # Centra todo el contenido de la columna
    )

    cargar_datos() # Esto se ejecuta cada vez que llamamos a HomeView(page)
    return content