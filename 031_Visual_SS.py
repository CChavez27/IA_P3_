import flet as ft   #Importamos flamework para el desarollo de la interfaz
import random       #Importamos la libreria random
import time         #Importamos la libreria time

def main(page: ft.Page):    #Se encargara de generar la ventana 

    def create_containers (number): #Funcion que creara nuestros contenedores y cuantos seran con el parametro number
        container_list = []         #Variable donde retornara 
        for _ in range(number):     #Numero de veces que generara 
            container_list.append(  #
                ft.Container(       #El diseno y contenido que tendra nuestro container
                    content = ft.Text(value = random.randint(1,100)),   #Tendra dentro del container un numero random del 1 al 100
                    alignment = ft.alignment.center,                  #Alinea el numero en el centro de la figura
                    width = 75,                                       #Definimos la anchura que tendra nuestro container
                    height = 75,                                      #Definimos la altura que tendra nuestro container
                    bgcolor = ft.colors.RED,                       #Definimos el color de fondo del container a naranja
                    border_radius = 50,                               # Hacemos que los bordes del contenedor sean redondeados con el radio
                )
            )
        return container_list       #Return cuando haya finalizado de crear su primer container pasar al siguiente 
    
    row = ft.Row(controls=create_containers (10))   #Le decimos cuantos contenedores se hagan
    page.add(row)   #Agrega los contenedores de manera horizontal en la ventana

    time.sleep(1)   #
    
    arr = row.controls  #Definimos el arreglo 

#Logica del ordenamiento por seleccion
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            
            arr[j-1].bgcolor = ft.colors.RED
            arr[min_idx].bgcolor = ft.colors.BLUE_900
            arr[j].bgcolor = ft.colors.ORANGE  # Cambiamos el color del contenedor actual a naranja
            time.sleep(1)  # Pausa de 0.5 segundos para visualizar el cambio
            page.update()  # Actualizamos la página con los cambios
            if int(arr[j].content.value) < int(arr[min_idx].content.value):
                arr[min_idx].bgcolor = ft.colors.RED
                min_idx = j
                arr[j].bgcolor = ft.colors.RED
               
        arr[j].bgcolor = ft.colors.RED
        arr[min_idx].bgcolor = ft.colors.GREEN	  # Cambiamos el color del contenedor más pequeño encontrado a azul
        page.update()  # Actualizamos la página para mostrar el cambio
        time.sleep(1)  # Pausa de 0.5 segundos para visualizar el cambio        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Intercambiamos los contenedores
        arr[i].bgcolor = ft.colors.GREEN  # Cambiamos el color del contenedor ordenado a verde

#Finaliza lo logica

    page.update()  #Actualiza la pagina con los cambios que se hicieron

ft.app(target = main)     #Genera la ventana con la logica que haya en main
