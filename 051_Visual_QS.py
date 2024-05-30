import flet as ft  # Importamos flamework para el desarrollo de la interfaz
import random  # Importamos la librería random
import time  # Importamos la librería time

def main(page: ft.Page):  # Se encargará de generar la ventana

    def create_containers(number):  # Función que creará nuestros contenedores y cuántos serán con el parámetro number
        container_list = []  # Variable donde retornará
        for _ in range(number):  # Número de veces que generará
            container_list.append(  #
                ft.Container(  # El diseño y contenido que tendrá nuestro container
                    content=ft.Text(value=str(random.randint(1, 100))),  # Tendrá dentro del container un número random del 1 al 100
                    alignment=ft.alignment.center,  # Alinea el número en el centro de la figura
                    width=75,  # Definimos la anchura que tendrá nuestro container
                    height=75,  # Definimos la altura que tendrá nuestro container
                    bgcolor=ft.colors.RED,  # Definimos el color de fondo del container a rojo
                    border_radius=50,  # Hacemos que los bordes del contenedor sean redondeados con el radio
                )
            )
        return container_list  # Retorna cuando haya finalizado de crear su primer container para pasar al siguiente
    time.sleep(2)   #
    def quick_sort(arr, low, high, container_list):
        if low < high:
            pi = partition(arr, low, high, container_list)
            quick_sort(arr, low, pi - 1, container_list)
            quick_sort(arr, pi + 1, high, container_list)

    def partition(arr, low, high, container_list):
        pivot = arr[high]
        container_list[high].bgcolor = ft.colors.BLUE  # Resalta el pivote
        page.update()
        time.sleep(3.5)

        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
                container_list[i].content.value, container_list[j].content.value = container_list[j].content.value, container_list[i].content.value
                container_list[i].bgcolor = ft.colors.GREEN  # Resalta el intercambio
                container_list[j].bgcolor = ft.colors.GREEN  # Resalta el intercambio
                page.update()
                time.sleep(3.5)
                container_list[i].bgcolor = ft.colors.RED  # Regresa al color original
                container_list[j].bgcolor = ft.colors.RED  # Regresa al color original
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        container_list[i + 1].content.value, container_list[high].content.value = container_list[high].content.value, container_list[i + 1].content.value
        container_list[i + 1].bgcolor = ft.colors.BLUE  # Resalta el intercambio final
        container_list[high].bgcolor = ft.colors.BLUE  # Resalta el intercambio final
        page.update()
        time.sleep(3.5)
        container_list[i + 1].bgcolor = ft.colors.GREEN  # Regresa al color original
        container_list[high].bgcolor = ft.colors.GREEN  # Regresa al color original

        return i + 1

    row = ft.Row(controls=create_containers(8))  # Le decimos cuántos contenedores se hagan
    page.add(row)  # Agrega los contenedores de manera horizontal en la ventana

    arr = [int(container.content.value) for container in row.controls]  # Definimos el arreglo

    quick_sort(arr, 0, len(arr) - 1, row.controls)  # Lógica del ordenamiento Quick Sort

    page.update()  # Actualiza la página con los cambios que se hicieron
    time.sleep(3)
ft.app(target=main)  # Genera la ventana con la lógica que haya en main
