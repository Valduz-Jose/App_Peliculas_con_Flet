import flet as ft
from services.pelicula_service import PeliculaService

def HomeView(page: ft.Page):
    titulo = ft.Row(
        controls=[
            ft.Icon(ft.Icons.MOVIE, size=30, color=ft.Colors.AMBER),
            ft.Text("Catálogo de Películas", size=24, weight="bold")
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Título")),
            ft.DataColumn(ft.Text("Director")),
            ft.DataColumn(ft.Text("Puntuación")),
            ft.DataColumn(ft.Text("Acciones")),
        ],
        border=ft.border.all(1, ft.Colors.BLUE_GREY_700),
        border_radius=10,
    )

    def borrar_click(id):
        if PeliculaService.eliminar(id):
            cargar_datos()
            page.snack_bar = ft.SnackBar(ft.Text("🗑️ Película eliminada"))
            page.snack_bar.open = True
            page.update()

    def ir_a_editar(id):
        # USAMOS ATRIBUTO DIRECTO (Inmune a errores de Session)
        page.id_pelicula_editar = id 
        page.navigation_bar.selected_index = 1
        # Llamamos a la función de cambio manualmente
        page.navigation_bar.on_change(None)

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
                                ft.IconButton(ft.Icons.EDIT, icon_color="blue", on_click=lambda _, id=peli_id: ir_a_editar(id)),
                                ft.IconButton(ft.Icons.DELETE, icon_color="red", on_click=lambda _, id=peli_id: borrar_click(id)),
                            ])
                        ),
                    ]
                )
            )
        page.update()

    cargar_datos()

    return ft.Column(
        controls=[
            titulo,
            ft.Divider(height=20, color="transparent"),
            ft.Row([tabla], alignment=ft.MainAxisAlignment.CENTER)
        ],
        expand=True,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )