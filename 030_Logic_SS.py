def Ordenamiento_Seleccion(arr):#Definimos nuestra funcion y Arreglo
    n = len(arr)    #Las veces que repetira la comparacion
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:    #Si mi arreglo en la posicion j es menor que el arreglo que la posicion j+1 
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

lista = [45,1,47,89,100]            #Creamos nuestra lista
Ordenamiento_Seleccion(lista)         #Utilizamos la funcion y el argumento lista
print(lista)                        #Imprimimos nuestra lista
