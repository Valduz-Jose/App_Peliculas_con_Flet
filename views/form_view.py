import flet as ft
from services.pelicula_service import PeliculaService

def FormView(page: ft.Page):
    # GET: mostrar formulario vacío
    
    # Campos de texto
    tf_titulo = ft.TextField(
        label="Título de la película", 
        hint_text="Ej: Interestelar", 
        expand=True,
        border_color=ft.Colors.BLUE_GREY_400
    )
    tf_director = ft.TextField(
        label="Director", 
        hint_text="Ej: Christopher Nolan", 
        expand=True,
        border_color=ft.Colors.BLUE_GREY_400
    )
    tf_puntuacion = ft.TextField(
        label="Puntuación (1-10)", 
        hint_text="Ej: 9", 
        expand=True,
        border_color=ft.Colors.BLUE_GREY_400
    )

    def guardar_click(e):
        # POST: procesar y guardar
        # 1. Validación simple de campos vacíos
        if not tf_titulo.value or not tf_director.value or not tf_puntuacion.value:
            page.snack_bar = ft.SnackBar(
                ft.Text("⚠️ Por favor, rellena todos los campos"),
                bgcolor=ft.Colors.ORANGE_700
            )
            page.snack_bar.open = True
            page.update()
            return

        # 2. Intentar guardar mediante el servicio
        try:
            puntuacion_int = int(tf_puntuacion.value)
            exito = PeliculaService.crear(
                titulo=tf_titulo.value,
                director=tf_director.value,
                puntuacion=puntuacion_int
            )

            if exito:
                page.snack_bar = ft.SnackBar(
                    ft.Text("✅ ¡Película guardada correctamente!"),
                    bgcolor=ft.Colors.GREEN_700
                )
                page.snack_bar.open = True
                
                # Limpiar el formulario
                tf_titulo.value = ""
                tf_director.value = ""
                tf_puntuacion.value = ""
                
                # Opcional: Volver al inicio después de guardar
                # page.navigation_bar.selected_index = 0
                # page.on_route_change(None) # Si tuvieras router, aquí disparamos el cambio
                
                page.update()
        
        except ValueError:
            page.snack_bar = ft.SnackBar(
                ft.Text("❌ La puntuación debe ser un número entero"),
                bgcolor=ft.Colors.RED_700
            )
            page.snack_bar.open = True
            page.update()

    def cancelar_click(e):
        # Volver al Home (En este diseño, reseteamos al índice 0 de la navbar manualmente)
        page.navigation_bar.selected_index = 0
        # Forzamos el evento on_change de la navbar para que app.py cambie la vista
        page.navigation_bar.on_change(
            ft.NavigationBarChangeEvent(control=page.navigation_bar, selected_index=0)
        )

    # Botones
    btn_guardar = ft.ElevatedButton(
        "Guardar Película",
        icon=ft.Icons.SAVE,
        style=ft.ButtonStyle(bgcolor=ft.Colors.AMBER, color=ft.Colors.BLACK),
        on_click=guardar_click
    )
    
    btn_cancelar = ft.TextButton(
        "Cancelar",
        on_click=cancelar_click
    )

    # Contenedor del formulario con diseño centrado y adaptable
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Icon(ft.Icons.ADD_CHART, size=40, color=ft.Colors.AMBER),
                ft.Text("Registrar Nueva Película", size=20, weight=ft.FontWeight.BOLD),
                ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                tf_titulo,
                tf_director,
                tf_puntuacion,
                ft.Row(
                    [btn_guardar, btn_cancelar], 
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            width=400
        ),
        alignment=ft.Alignment(0, 0), # [CORREGIDO] Uso de MAYÚSCULAS
        expand=True
    )