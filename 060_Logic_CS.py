def countSort(arr):
    output = [0 for i in range(len(arr))]   #Hacemos un arreglo del tamano original
    count = [0 for i in range(10)]          #Arreglo que usaremos para contar del tamano del elemento mas grande
  
    #Contamos cuantas veces aparece cada numero
    for i in arr:
        count[i] += 1
    
    #Hacemos la suma comparativa
    for i in range(1, 10):
        count[i] += count[i-1]
  
    #Contruimos nuestro arreglo resultante
    for i in range(len(arr)):
        output[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1
    return output
 
arr = [1, 4, 1, 2, 7, 5, 2]
ans = countSort(arr)
print(ans)
