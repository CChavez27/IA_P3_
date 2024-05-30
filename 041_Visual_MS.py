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

    def merge_sort(arr, container_list):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]
            left_containers = container_list[:mid]
            right_containers = container_list[mid:]

            merge_sort(left_half, left_containers)
            merge_sort(right_half, right_containers)

            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    container_list[k].content.value = str(left_half[i])
                    container_list[k].bgcolor = ft.colors.ORANGE  # Cambiamos el color del contenedor a verde
                    
                    page.update()
                    time.sleep(2.5)  # Para mostrar visualmente el proceso
                    container_list[k].bgcolor = ft.colors.GREEN  # Regresamos el color del contenedor a rojo
                    i += 1
                else:
                    arr[k] = right_half[j]
                    container_list[k].content.value = str(right_half[j])
                    container_list[k].bgcolor = ft.colors.ORANGE  # Cambiamos el color del contenedor a azul
                    page.update()
                    time.sleep(2.5)  # Para mostrar visualmente el proceso
                    container_list[k].bgcolor = ft.colors.GREEN  # Regresamos el color del contenedor a rojo
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                container_list[k].content.value = str(left_half[i])
                container_list[k].bgcolor = ft.colors.ORANGE  # Cambiamos el color del contenedor a verde
                page.update()
                time.sleep(2.5)  # Para mostrar visualmente el proceso
                container_list[k].bgcolor = ft.colors.ORANGE  # Regresamos el color del contenedor a rojo
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                container_list[k].content.value = str(right_half[j])
                container_list[k].bgcolor = ft.colors.RED  # Cambiamos el color del contenedor a azul
                page.update()
                time.sleep(2.5)  # Para mostrar visualmente el proceso
                container_list[k].bgcolor = ft.colors.ORANGE  # Regresamos el color del contenedor a rojo
                j += 1
                k += 1

    row = ft.Row(controls=create_containers(8))  # Le decimos cuántos contenedores se hagan
    page.add(row)  # Agrega los contenedores de manera horizontal en la ventana
    time.sleep(2)   #
    arr = [int(container.content.value) for container in row.controls]  # Definimos el arreglo

    merge_sort(arr, row.controls)  # Lógica del ordenamiento Merge sort

    page.update()  # Actualiza la página con los cambios que se hicieron

ft.app(target=main)  # Genera la ventana con la lógica que haya en main
