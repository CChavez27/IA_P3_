import flet as ft  # Importamos flamework para el desarrollo de la interfaz
import random  # Importamos la librería random
import time  # Importamos la librería time

def main(page: ft.Page):  # Se encargará de generar la ventana

    def create_containers(number):  # Función que creará nuestros contenedores y cuántos serán con el parámetro number
        container_list = []  # Variable donde retornará
        for _ in range(number):  # Número de veces que generará
            container_list.append(  #
                ft.Container(  # El diseño y contenido que tendrá nuestro container
                    content=ft.Text(value=str(random.randint(0, 9))),  # Tendrá dentro del container un número random del 0 al 9
                    alignment=ft.alignment.center,  # Alinea el número en el centro de la figura
                    width=75,  # Definimos la anchura que tendrá nuestro container
                    height=75,  # Definimos la altura que tendrá nuestro container
                    bgcolor=ft.colors.RED,  # Definimos el color de fondo del container a rojo
                    border_radius=50,  # Hacemos que los bordes del contenedor sean redondeados con el radio
                )
            )
        return container_list  # Retorna cuando haya finalizado de crear su primer container para pasar al siguiente

    def count_sort(arr, container_list):
        max_val = max(arr)
        count = [0] * (max_val + 1)
        output = [0] * len(arr)

        # Contamos cuántas veces aparece cada número
        for i in arr:
            count[i] += 1
            container_list[i].bgcolor = ft.colors.BLUE  # Resaltamos el contenedor que estamos contando
            page.update()
            time.sleep(1.5)

        # Hacemos la suma comparativa
        for i in range(1, len(count)):
            count[i] += count[i - 1]

        # Construimos nuestro arreglo resultante
        for i in range(len(arr) - 1, -1, -1):
            output[count[arr[i]] - 1] = arr[i]
            container_list[count[arr[i]] - 1].content.value = str(arr[i])
            container_list[count[arr[i]] - 1].bgcolor = ft.colors.GREEN  # Resaltamos el contenedor donde se coloca el elemento
            page.update()
            time.sleep(4.5)
            count[arr[i]] -= 1

        for i in range(len(arr)):
            arr[i] = output[i]
            container_list[i].content.value = str(output[i])
            container_list[i].bgcolor = ft.colors.BLUE  # Resaltamos el contenedor final
            page.update()
            time.sleep(4.5)

    row = ft.Row(controls=create_containers(10))  # Le decimos cuántos contenedores se hagan
    page.add(row)  # Agrega los contenedores de manera horizontal en la ventana

    arr = [int(container.content.value) for container in row.controls]  # Definimos el arreglo

    count_sort(arr, row.controls)  # Lógica del ordenamiento Counting Sort

    page.update()  # Actualiza la página con los cambios que se hicieron

ft.app(target=main)  # Genera la ventana con la lógica que haya en main
