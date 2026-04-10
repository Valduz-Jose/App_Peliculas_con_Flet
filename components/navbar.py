import flet as ft

def Navbar(on_change):
    return ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icons.LIST_ALT, 
                label="Inicio"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.ADD_CIRCLE_OUTLINE, 
                selected_icon=ft.Icons.ADD_CIRCLE, 
                label="Agregar"
            ),
        ],
        on_change=on_change,
        bgcolor=ft.Colors.BLUE_GREY_800,
        selected_index=0,
    )