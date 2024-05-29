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

#Logica del ordenamiento Insercion
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        key_value = int(key.content.value)  # Guardamos el valor del contenedor actual
        key.bgcolor = ft.colors.ORANGE  # Resaltamos el contenedor actual en azul
        
        j = i - 1
        arr[j].bgcolor = ft.colors.ORANGE  # Resaltamos el contenedor que estamos comparando en naranja
        page.update()  #Actualiza la pagina con los cambios que se hicieron
        time.sleep(4)

        while j >= 0 and key_value < int(arr[j].content.value):
            arr[j].bgcolor = ft.colors.ORANGE  # Resaltamos el contenedor que estamos comparando en naranja
            page.update()  #Actualiza la pagina con los cambios que se hicieron

            arr[j + 1].content.value = arr[j].content.value  # Movemos el valor del contenedor
            
            j -= 1
            arr[j + 1].bgcolor = ft.colors.BLUE
            time.sleep(1)
            page.update()  #Actualiza la pagina con los cambios que se hicieron
            arr[j + 1].bgcolor = ft.colors.ORANGE
            time.sleep(1)

        arr[j + 1].content.value = key_value  # Insertamos el valor del contenedor en su posición correcta
        page.update()  #Actualiza la pagina con los cambios que se hicieron

    for container in arr:
        container.bgcolor = ft.colors.GREEN
    page.update()  #Actualiza la pagina con los cambios que se hicieron
    time.sleep(0.5)
#Finaliza lo logica
   
    page.update()  #Actualiza la pagina con los cambios que se hicieron
    
ft.app(target = main)     #Genera la ventana con la logica que haya en main
