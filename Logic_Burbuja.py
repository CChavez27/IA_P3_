
def ordenamiento_burbuja (arr):     #Definimos nuestra funcion y Arreglo
    n = len(arr)                    #Las veces que repetira la comparacion
    for i in range(n):              #Comparara el 
        for j in range(0, n-i-1):   #Acorta la lista al ordenar
            if arr[j] > arr[j + 1]: #Si mi arreglo en la posicion j es mayor que el arreglo que la posicion j+1 
                arr[j], arr[j + 1] = arr[j+1], arr[j]   #Se hace el intercambio de posicion 

lista = [45,1,47,89,100]            #Creamos nuestra lista

ordenamiento_burbuja(lista)         #Utilizamos la funcion y el argumento lista
print(lista)                        #Imprimimos nuestra lista