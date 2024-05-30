import flet as ft  # Importamos flamework para el desarrollo de la interfaz
import random  # Importamos la librería random
import time  # Importamos la librería time

def main(page: ft.Page):  # Se encargará de generar la ventana

    def create_containers(number):  # Función que creará nuestros contenedores y cuántos serán con el parámetro number
        container_list = []  # Variable donde retornará
        for _ in range(number):  # Número de veces que generará
            container_list.append(  #
                ft.Container(  # El diseño y contenido que tendrá nuestro container
                    content=ft.Text(value=str(random.randint(1, 999))),  # Tendrá dentro del container un número random del 1 al 999
                    alignment=ft.alignment.center,  # Alinea el número en el centro de la figura
                    width=75,  # Definimos la anchura que tendrá nuestro container
                    height=75,  # Definimos la altura que tendrá nuestro container
                    bgcolor=ft.colors.RED,  # Definimos el color de fondo del container a rojo
                    border_radius=50,  # Hacemos que los bordes del contenedor sean redondeados con el radio
                )
            )
        return container_list  # Retorna cuando haya finalizado de crear su primer container para pasar al siguiente

    def counting_sort(arr, exp, container_list):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = arr[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(len(arr)):
            arr[i] = output[i]
            container_list[i].content.value = str(output[i])
            container_list[i].bgcolor = ft.colors.GREEN  # Resaltamos el contenedor donde se coloca el elemento
            page.update()
            time.sleep(1.5)
            
            if exp == 100:  # Si estamos ordenando por las centenas, cambiamos a verde
                container_list[i].bgcolor = ft.colors.GREEN
            elif exp == 10:  # Si estamos ordenando por las decenas, cambiamos a azul
                container_list[i].bgcolor = ft.colors.BLUE
            else:  # Para las unidades, usamos naranja
                container_list[i].bgcolor = ft.colors.ORANGE

    def radix_sort(arr, container_list):
        max_val = max(arr)

        exp = 1
        while max_val // exp > 0:
            counting_sort(arr, exp, container_list)
            exp *= 10

    row = ft.Row(controls=create_containers(10))  # Le decimos cuántos contenedores se hagan
    page.add(row)  # Agrega los contenedores de manera horizontal en la ventana

    arr = [int(container.content.value) for container in row.controls]  # Definimos el arreglo

    radix_sort(arr, row.controls)  # Lógica del ordenamiento Radix Sort

    page.update()  # Actualiza la página con los cambios que se hicieron

ft.app(target=main)  # Genera la ventana con la lógica que haya en main
