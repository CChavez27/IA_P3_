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

    time.sleep(4)   #
    
    arr = row.controls  #Definimos el arreglo 

#Logica del ordenamiento burbuja
    n = len(arr)                    #Las veces que repetira la comparacion
    for i in range(n):              #Comparara el 
        for j in range(0, n-i-1):   #Acorta la veces que se va acompara al ordenar 
            arr[j].bgcolor = ft.colors.ORANGE
            arr[j + 1].bgcolor = ft.colors.ORANGE
            time.sleep(0.5)
            page.update()  #Actualiza la pagina con los cambios que se hicieron 
            if int (arr[j].content.value) > int(arr[j + 1].content.value) : #Si mi valor del arreglo en la posicion j es mayor que el arreglo que la posicion j+1 
                arr[j], arr[j + 1] = arr[j + 1], arr[j]   #Se hace el intercambio de posicion 
            arr[j].bgcolor = ft.colors.RED
            arr[j + 1].bgcolor = ft.colors.RED
        arr[n-i-1].bgcolor = ft.colors.GREEN
#Finaliza lo logica

    page.update()  #Actualiza la pagina con los cambios que se hicieron

ft.app(target = main)     #Genera la ventana con la logica que haya en main