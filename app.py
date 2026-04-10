import flet as ft
from database import Session # [NUEVO]
from models.pelicula import Pelicula # [NUEVO]

# --- LÓGICA DE NEGOCIO (SERVICIO TEMPORAL) ---
def obtener_todas_las_peliculas():
    # [NUEVO] Consulta a la base de datos
    session = Session()
    try:
        peliculas = session.query(Pelicula).all()
        return peliculas
    finally:
        session.close()

def main(page: ft.Page):
    page.title = "🎞️ Flet Películas"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.BLUE_GREY_900
    page.padding = 20
    
    # Alineación superior para el listado
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Título de la aplicación
    titulo = ft.Row(
        controls=[
            ft.Icon(ft.Icons.MOVIE, size=30, color=ft.Colors.AMBER),
            ft.Text("Catálogo de Películas", size=24, weight=ft.FontWeight.BOLD)
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    # Definición de la Tabla (DataTable)
    tabla = ft.DataTable(
        expand=True,
        border=ft.border.all(1, ft.Colors.BLUE_GREY_700),
        border_radius=10,
        heading_row_color=ft.Colors.BLUE_GREY_800,
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Título")),
            ft.DataColumn(ft.Text("Director")),
            ft.DataColumn(ft.Text("Puntuación", text_align=ft.TextAlign.RIGHT)),
        ],
        rows=[]
    )

    # Función para cargar datos en la tabla
    def cargar_datos():
        peliculas = obtener_todas_las_peliculas()
        tabla.rows.clear()
        for peli in peliculas:
            tabla.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(peli.id))),
                        ft.DataCell(ft.Text(peli.titulo)),
                        ft.DataCell(ft.Text(peli.director)),
                        ft.DataCell(ft.Text(str(peli.puntuacion))),
                    ]
                )
            )
        page.update()

    # Contenedor para que la tabla sea adaptable
    listado_container = ft.Column(
        controls=[tabla],
        scroll=ft.ScrollMode.ADAPTIVE,
        expand=True
    )

    page.add(titulo, ft.Divider(height=20, color=ft.Colors.TRANSPARENT), listado_container)
    
    # Cargar los datos al iniciar
    cargar_datos()

if __name__ == "__main__":
    ft.run(main)