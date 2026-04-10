import flet as ft
from services.pelicula_service import PeliculaService

def FormView(page: ft.Page):
    # RECUPERAMOS EL ATRIBUTO PERSONALIZADO
    id_editar = getattr(page, "id_pelicula_editar", None)
    
    tf_titulo = ft.TextField(label="Título", expand=True)
    tf_director = ft.TextField(label="Director", expand=True)
    tf_puntuacion = ft.TextField(label="Puntuación (1-10)", expand=True)

    if id_editar:
        peli = PeliculaService.obtener_por_id(id_editar)
        if peli:
            tf_titulo.value = peli.titulo
            tf_director.value = peli.director
            tf_puntuacion.value = str(peli.puntuacion)

    def guardar_click(e):
        if not tf_titulo.value or not tf_director.value or not tf_puntuacion.value:
            return

        try:
            if id_editar:
                exito = PeliculaService.actualizar(id_editar, tf_titulo.value, tf_director.value, int(tf_puntuacion.value))
                # Limpiamos el atributo después de editar
                page.id_pelicula_editar = None
            else:
                exito = PeliculaService.crear(tf_titulo.value, tf_director.value, int(tf_puntuacion.value))
            
            if exito:
                page.snack_bar = ft.SnackBar(ft.Text("✅ Operación exitosa"), bgcolor="green")
                page.snack_bar.open = True
                page.navigation_bar.selected_index = 0
                page.navigation_bar.on_change(None) 
                page.update()
        except Exception as err:
            print(f"Error en el formulario: {err}")

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Editar Película" if id_editar else "Nueva Película", size=24, weight="bold"),
                tf_titulo, tf_director, tf_puntuacion,
                ft.ElevatedButton("Guardar", icon=ft.Icons.SAVE, on_click=guardar_click, bgcolor="amber", color="black")
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            width=400,
            spacing=20
        ),
        alignment=ft.Alignment(0, 0),
        expand=True
    )