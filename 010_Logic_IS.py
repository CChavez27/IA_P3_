def Ordenamiento_Insercion(arr):    #Definimos nuestra funcion y Arreglo
    n = len(arr)                    #Las veces que repetira la comparacion
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

lista = [45,1,47,89,100]            #Creamos nuestra lista
Ordenamiento_Insercion(lista)         #Utilizamos la funcion y el argumento lista
print(lista)                        #Imprimimos nuestra lista       
