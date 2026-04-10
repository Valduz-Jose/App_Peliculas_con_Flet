import flet as ft
from services.pelicula_service import PeliculaService

def FormView(page: ft.Page):
    # Definición de campos
    tf_titulo = ft.TextField(label="Título", expand=True)
    tf_director = ft.TextField(label="Director", expand=True)
    tf_puntuacion = ft.TextField(label="Puntuación (1-10)", expand=True)

    def guardar_click(e):
        if not tf_titulo.value or not tf_director.value or not tf_puntuacion.value:
            return

        try:
            exito = PeliculaService.crear(
                tf_titulo.value, 
                tf_director.value, 
                int(tf_puntuacion.value)
            )
            
            if exito:
                # 1. Limpiar campos para la próxima vez
                tf_titulo.value = ""
                tf_director.value = ""
                tf_puntuacion.value = ""
                
                # 2. Configurar SnackBar (Versión antigua/segura)
                snack = ft.SnackBar(
                    content=ft.Text("✅ ¡Guardado con éxito!"),
                    bgcolor=ft.Colors.GREEN_700
                )
                page.snack_bar = snack
                page.snack_bar.open = True
                
                # 3. REDIRECCIÓN SEGURA:
                # Cambiamos el índice visualmente
                page.navigation_bar.selected_index = 0
                
                # Buscamos la función de cambio que está en app.py a través de la página
                # En Flet, podemos acceder a la función on_change de la barra directamente
                page.navigation_bar.on_change(e) 
                
                page.update()

        except Exception as err:
            print(f"Error en vista: {err}")

        except ValueError:
            print("Error: Puntuación no es número")

    def mostrar_mensaje(texto, color):
        # Forma tradicional compatible
        page.snack_bar = ft.SnackBar(
            content=ft.Text(texto),
            bgcolor=color
        )
        page.snack_bar.open = True
        page.update()

    btn_guardar = ft.ElevatedButton(
        "Guardar Película", 
        icon=ft.Icons.SAVE, 
        on_click=guardar_click,
        style=ft.ButtonStyle(bgcolor=ft.Colors.AMBER, color=ft.Colors.BLACK)
    )

    # El diseño final (usando el fix de Alignment que funcionó)
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Registrar Nueva Película", size=24, weight="bold"),
                tf_titulo, tf_director, tf_puntuacion,
                btn_guardar
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            width=400,
            spacing=20
        ),
        alignment=ft.Alignment(0, 0), 
        expand=True
    )